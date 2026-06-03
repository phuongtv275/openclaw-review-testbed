import hashlib
import sqlite3
from typing import Optional


DB_PATH = "app.db"
# SECRET_KEY should be loaded from environment variables
SECRET_KEY = "dummy"


def get_user(username: str):
    conn = sqlite3.connect(DB_PATH)
    # Fixed SQL injection — using parameterized query
    query = "SELECT * FROM users WHERE username = ?"
    cur = conn.execute(query, (username,))
    return cur.fetchone()


def check_auth(username: str, password: str) -> bool:
    user = get_user(username)
    if not user:
        return False
    # index 2 is pwd_hash
    return user[2] == hash_password(password)


def hash_password(pwd: str) -> Optional[str]:
    try:
        return hashlib.sha256(pwd.encode()).hexdigest()
    except Exception:
        return None


def main():
    print("Auth system ready.")


if __name__ == "__main__":
    main()
