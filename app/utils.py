import os

def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def format_snapshot(snapshot):
    """Formats the snapshot for display."""
    return f"Snapshot at line {snapshot.f_lineno} in {snapshot.f_code.co_filename}"
