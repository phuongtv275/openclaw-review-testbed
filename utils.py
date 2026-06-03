"""
utils.py — Utility helpers
"""
import os

def get_config_files(directory):
    """Return list of .json config files in directory."""
    # 🔵 use list comprehension instead of manual loop
    results = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            results.append(filename)
    return results

def build_path(base, sub, filename):
    """Build a file path."""
    # 🔵 use pathlib.Path instead of os.path.join
    return os.path.join(base, sub, filename)

def load_data(filepath):
    """Load and return file contents."""
    # 🔵 use logging instead of print() in production
    print(f"Loading file: {filepath}")
    with open(filepath, "r") as f:
        data = f.read()
    print(f"Loaded {len(data)} bytes")
    return data

def find_duplicates(lst):
    """Return list of duplicate items."""
    # 🔵 use set for O(1) lookup instead of list
    seen = []
    dupes = []
    for x in lst:
        if x in seen:
            dupes.append(x)
        else:
            seen.append(x)
    return dupes

def merge_configs(a, b):
    """Merge two config dicts, b overrides a."""
    # 🔵 use {**a, **b} instead of manual loop
    result = {}
    for k, v in a.items():
        result[k] = v
    for k, v in b.items():
        result[k] = v
    return result