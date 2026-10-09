import importlib.util
import os
from pathlib import Path
import secrets
import sys
import time
import unittest
from unittest.mock import patch

APP_DIR = Path(__file__).resolve().parents[1] / 'app'
sys.path.insert(0, str(APP_DIR))
for name in ('FLASK_SECRET_KEY', 'OIDC_CLIENT_SECRET', 'DB_PASSWORD'):
    os.environ[name] = secrets.token_hex(32)
os.environ.update(OIDC_CLIENT_ID='test-client', OIDC_DISCOVERY_URL='https://identity.example.invalid/.well-known/openid-configuration', DB_HOST='127.0.0.1', DB_NAME='synthetic', DB_USER='test-role', LAB_HTTP_ONLY='1')
spec = importlib.util.spec_from_file_location('portal', APP_DIR / 'app.py')
portal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(portal)
portal.app.config.update(TESTING=True)

class RouteBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.client = portal.app.test_client()
    def login(self, roles, expired=False):
        with self.client.session_transaction() as session:
            session['user'] = {'sub': 'synthetic-id', 'preferred_username': 'synthetic-user'}
            session['portal_roles'] = roles
            session['expires_at'] = time.time() + (-1 if expired else 300)
    def test_anonymous_admin_redirects(self):
        with patch.object(portal, 'get_db') as db:
            response = self.client.get('/admin')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, '/login')
            db.assert_not_called()
    def test_employee_admin_denied_before_database_access(self):
        self.login(['employee'])
        with patch.object(portal, 'get_db') as db:
            self.assertEqual(self.client.get('/admin').status_code, 403)
            db.assert_not_called()
    def test_malformed_claims_deny_admin(self):
        self.login('portal-admin')
        self.assertEqual(self.client.get('/admin').status_code, 403)
    def test_admin_allowed_with_synthetic_database(self):
        self.login(['portal-admin'])
        with patch.object(portal, 'get_db') as db, patch.object(portal, 'render_template', return_value='synthetic records'):
            self.assertEqual(self.client.get('/admin').status_code, 200)
            db.return_value.cursor.return_value.execute.assert_called_once_with('SELECT * FROM configs')
    def test_employee_business_route_allowed(self):
        self.login(['employee'])
        with patch.object(portal, 'get_db'), patch.object(portal, 'render_template', return_value='synthetic records'):
            self.assertEqual(self.client.get('/employee').status_code, 200)
    def test_expired_session_requires_login(self):
        self.login(['portal-admin'], expired=True)
        with patch.object(portal, 'get_db') as db:
            self.assertEqual(self.client.get('/admin').status_code, 302)
            db.assert_not_called()

if __name__ == '__main__': unittest.main()
