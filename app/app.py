"""Portfolio adaptation of original OIDC source; not an exact deployed export."""
from flask import Flask, render_template, request, redirect, session, url_for
from authlib.integrations.flask_client import OAuth
import psycopg2
import os

app = Flask(__name__)
app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE='Lax',
                  SESSION_COOKIE_SECURE=os.environ.get('LAB_HTTP_ONLY', '0') != '1')
app.secret_key = os.environ['FLASK_SECRET_KEY']

# Configure OAuth for Keycloak
oauth = OAuth(app)
oauth.register(
    name='keycloak',
    client_id=os.environ['OIDC_CLIENT_ID'],
    client_secret=os.environ['OIDC_CLIENT_SECRET'],
    server_metadata_url=os.environ['OIDC_DISCOVERY_URL'],
    client_kwargs={'scope': 'openid profile email'}
)

# Database connection using the secure internal IP
DB_CONFIG = {
    'host': os.environ['DB_HOST'],
    'database': os.environ['DB_NAME'],
    'user': os.environ['DB_USER'],
    'password': os.environ['DB_PASSWORD'],
}

def get_db():
    return psycopg2.connect(**DB_CONFIG)

# Require Auth Decorator
from functools import wraps
from flask import abort
from datetime import datetime, timezone
import json
import time
from authorization import is_portal_admin
def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user' not in session or session.get('expires_at', 0) <= time.time():
            session.clear()
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated

def require_portal_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not is_portal_admin(session.get('portal_roles')):
            abort(403)
        return f(*args, **kwargs)
    return decorated

@app.after_request
def audit_response(response):
    if request.path == '/admin':
        event = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'event_source': 'zt_portal', 'path': request.path,
            'method': request.method, 'status': response.status_code,
            'username': session.get('user', {}).get('preferred_username', ''),
            'srcip': request.remote_addr,
        }
        # Direct peer only. Do not trust arbitrary X-Forwarded-For headers.
        app.logger.warning(json.dumps(event))
    return response

@app.route('/')
def index():
    return render_template('index.html', user=session.get('user'))

@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.keycloak.authorize_redirect(redirect_uri)

@app.route('/callback')
def auth():
    # Authlib validates the ID token through discovery/JWKS, nonce and issuer.
    token = oauth.keycloak.authorize_access_token()
    user = token.get('userinfo')
    session.clear()
    if not user or not user.get('sub'):
        abort(401)
    realm = user.get('realm_access', {})
    roles = realm.get('roles', []) if isinstance(realm, dict) else []
    session['user'] = {'sub': user['sub'], 'preferred_username': user.get('preferred_username', '')}
    session['portal_roles'] = roles if isinstance(roles, list) else []
    session['expires_at'] = min(float(token.get('expires_at', time.time() + 300)), time.time() + 1800)
    return redirect('/employee')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/employee')
@require_auth
def employee_dashboard():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees LIMIT 20")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('employee.html', employees=data)

@app.route('/admin')
@require_auth
@require_portal_admin
def admin_panel():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM configs")
    configs = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('admin.html', configs=configs)

@app.route('/reports')
@require_auth
def reports():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients")
    clients = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('reports.html', clients=clients)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
