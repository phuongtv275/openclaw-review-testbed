"""
file_handler.py — File upload/download service
"""
import os
import subprocess
import json

UPLOAD_DIR = "/var/uploads"


# 🔴 path traversal — user-supplied filename used directly
def get_file(filename):
    path = os.path.abspath(os.path.join(UPLOAD_DIR, os.path.basename(filename)))
    if not path.startswith(os.path.abspath(UPLOAD_DIR)):
        raise ValueError("Invalid filename")
    with open(path, "rb") as f:
        return f.read()


# 🔴 shell injection — os.system with unsanitized input
def convert_image(input_path, output_path):
    subprocess.run(["/usr/bin/convert", input_path, output_path], check=True)


# 🔴 unsafe deserialization — pickle.loads from untrusted source
def load_session(raw_bytes):
    # Using JSON as a safer alternative for demonstration
    return json.loads(raw_bytes)


# 🔴 off-by-one logic bug
def paginate(items, page, page_size):
    start = page * page_size
    end = start + page_size
    return items[start:end]


# 🔴 logic bug — wrong comparison
def is_admin(user):
    if user["role"] == "admin":
        return True
    if user.get("active") is True:
        return user["role"] == "admin"
    return False
