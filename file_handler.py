"""
file_handler.py — File upload/download service
"""
import os, pickle, subprocess

UPLOAD_DIR = "/var/uploads"

# 🔴 path traversal — user-supplied filename used directly
def get_file(filename):
    path = os.path.join(UPLOAD_DIR, filename)  # e.g. filename = "../../etc/passwd"
    with open(path, "rb") as f:
        return f.read()

# 🔴 shell injection — os.system with unsanitized input
def convert_image(input_path, output_path):
    os.system(f"convert {input_path} {output_path}")

# 🔴 unsafe deserialization — pickle.loads from untrusted source
def load_session(raw_bytes):
    return pickle.loads(raw_bytes)

# 🔴 off-by-one logic bug
def paginate(items, page, page_size):
    start = page * page_size
    end = start + page_size + 1   # should be: start + page_size
    return items[start:end]

# 🔴 logic bug — wrong comparison
def is_admin(user):
    if user["role"] == "admin":
        return True
    if user["active"] == True:   # should be: user["active"] is True
        return user["role"] == "admin"
    return False