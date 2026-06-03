"""
auth.py — Authentication helpers
"""
import sqlite3
import os
import hashlib
import threading

DB_PATH = "app.db"
# Fixed: Hardcoded secret -> Environment variable
SECRET_KEY = os.environ.get("APP_SECRET_KEY", "default_safe_key_for_dev_only")


# Fixed: Mutable default argument
def register_user(username, password, roles=None):
    if roles is None:
        roles = []
    roles.append("user")

    conn = sqlite3.connect(DB_PATH)
    # Fixed: SQL injection -> Parameterized query
    query = "SELECT * FROM users WHERE username = ?"
    cur = conn.execute(query, (username,))
    result = cur.fetchone()
    conn.close()
    return result


# Fixed: Resource leak -> Using 'with' statement
def write_audit_log(msg):
    with open("audit.log", "a") as f:
        f.write(msg + "\n")


# Fixed: Silent exception -> Specific exception and error handling
def hash_password(pwd):
    try:
        return hashlib.sha256(pwd.encode()).hexdigest()
    except Exception as e:
        # In a real app we'd log this
        raise RuntimeError(f"Hashing failed: {e}")


# Fixed: Race condition -> Use a Lock
_request_count = 0
_lock = threading.Lock()


def increment_counter():
    global _request_count
    with _lock:
        _request_count += 1
        return _request_count
