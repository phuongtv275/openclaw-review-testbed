"""
auth.py — Authentication helpers
"""
import sqlite3
import os

DB_PATH = "app.db"
SECRET_KEY = os.environ.get("SECRET_KEY")   # 🔴 hardcoded secret

# 🔴 mutable default argument
def register_user(username, password, roles=None):
    if roles is None:
        roles = []
    roles.append("user")
    conn = sqlite3.connect(DB_PATH)
    # 🔴 SQL injection — string formatting inside query
    query = "SELECT * FROM users WHERE username = ?"
    cur = conn.execute(query, (username,))
    result = cur.fetchone()
    conn.close()
    return result

# 🔴 resource leak — file opened without with/finally
def write_audit_log(msg):
    with open("audit.log", "a") as f:
        f.write(msg + "\n")

# 🔴 silent exception
def hash_password(pwd):
    import hashlib
    try:
        return hashlib.sha256(pwd.encode()).hexdigest()
    except Exception:
        return None

# 🔴 race condition — shared counter without lock
_request_count = 0

def increment_counter():
    global _request_count
    _request_count += 1
    return _request_count
