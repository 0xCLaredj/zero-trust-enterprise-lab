"""Intentionally unauthenticated historical lab baseline. Loopback only."""
from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

# Database connection (Phase 1: direct, no auth)
DB_CONFIG = {
    'host': os.environ['DB_HOST'],
    'database': os.environ['DB_NAME'],
    'user': os.environ['DB_USER'],
    'password': os.environ['DB_PASSWORD'],
}

def get_db():
    return psycopg2.connect(**DB_CONFIG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employee')
def employee_dashboard():
    # Phase 1: NO authentication check
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees LIMIT 20")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('employee.html', employees=data)

@app.route('/admin')
def admin_panel():
    # Phase 1: NO authentication check
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM configs")
    configs = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('admin.html', configs=configs)

@app.route('/reports')
def reports():
    # Phase 1: NO authentication check
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients")
    clients = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('reports.html', clients=clients)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
