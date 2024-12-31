from flask import Flask, render_template, request, jsonify
import os
from app.debugger import Debugger

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))

debugger = Debugger()  # Initialize a debugger instance.

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/load_snapshot", methods=["POST"])
def load_snapshot():
    snapshot_index = request.json.get("index")
    try:
        snapshot = debugger.load_snapshot(snapshot_index)  # Load the snapshot.
        response = {
            "status": "success",
            "snapshot": {
                "filename": snapshot.f_code.co_filename,
                "line_number": snapshot.f_lineno,
                "local_variables": snapshot.f_locals,
            }
        }
    except IndexError:
        response = {"status": "error", "message": "Snapshot not found."}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
