from flask import Flask, request, jsonify, render_template, send_from_directory
from app.debugger import Debugger
import os
import json

# Initialize Flask app and Debugger instance
app = Flask(__name__)
debugger = Debugger()  # This will load snapshots at startup

def is_json_serializable(value):
    """Check if a value is JSON serializable."""
    try:
        json.dumps(value)
        return True
    except (TypeError, OverflowError):
        return False



@app.route("/")
def index():
    # Get the list of snapshots to send to the frontend
    snapshots = debugger.snapshots
    return render_template("index.html", snapshots=snapshots)

@app.route("/load_snapshot", methods=["POST"])
def load_snapshot():
    try:
        # Log the incoming request data
        snapshot_index = request.json.get("index")
        print(f"Received snapshot index: {snapshot_index}")  # Debugging print

        # Validate the index
        if snapshot_index is None or not isinstance(snapshot_index, int):
            return jsonify({"status": "error", "message": "Invalid snapshot index."}), 400

        # Attempt to load the snapshot
        snapshot = debugger.load_snapshot(snapshot_index)
        print(f"Loaded snapshot data: {snapshot}")  # Debugging print

        # Sanitize local variables
        sanitized_locals = {
            key: str(value) if not is_json_serializable(value) else value
            for key, value in snapshot["local_variables"].items()
        }

        # Return the snapshot data
        return jsonify({
            "status": "success",
            "snapshot": {
                "filename": snapshot["filename"],
                "line_number": snapshot["line_number"],
                "local_variables": sanitized_locals,
            },
        })

    except IndexError as e:
        print(f"IndexError: {e}")  # Debugging print
        return jsonify({"status": "error", "message": "Snapshot index out of range."}), 400

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")  # Debugging print
        return jsonify({"status": "error", "message": "Snapshot file not found."}), 500

    except Exception as e:
        print(f"Unexpected Error: {e}")  # Debugging print
        return jsonify({"status": "error", "message": "Internal server error."}), 500



@app.route("/debug_file", methods=["POST"])
def debug_file():
    """Handle the request to start debugging a Python file."""
    file = request.files['file']
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)

    # Start debugging the file
    debugger.start_debugging(file_path)

    # Return the list of snapshot file paths to update the frontend dynamically
    return jsonify({
        "status": "success",
        "snapshots": debugger.snapshots  # Include the list of snapshots
    })


# Route to serve snapshot files (pkl files)
@app.route("/snapshots/<filename>")
def serve_snapshot(filename):
    snapshot_dir = os.path.join(os.getcwd(), "snapshots")
    return send_from_directory(snapshot_dir, filename)

if __name__ == "__main__":
    app.run(debug=True)
