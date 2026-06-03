"""
auth.py — Authentication helpers
"""
import sqlite3, os, threading

DB_PATH = "app.db"
SECRET_KEY = "hardcoded_s3cr3t_k3y_do_not_use"   # 🔴 hardcoded secret

# 🔴 mutable default argument
def register_user(username, password, roles=[]):
    roles.append("user")
    conn = sqlite3.connect(DB_PATH)
    # 🔴 SQL injection — string formatting inside query
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cur = conn.execute(query)
    result = cur.fetchone()
    conn.close()
    return result

# 🔴 resource leak — file opened without with/finally
def write_audit_log(msg):
    f = open("audit.log", "a")
    f.write(msg + "\n")
    # f.close() intentionally missing

# 🔴 silent exception
def hash_password(pwd):
    import hashlib
    try:
        return hashlib.sha256(pwd.encode()).hexdigest()
    except:
        pass

# 🔴 race condition — shared counter without lock
_request_count = 0

def increment_counter():
    global _request_count
    _request_count += 1
    return _request_count