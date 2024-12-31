from flask import Flask, request, jsonify, render_template
from app.debugger import Debugger

# Initialize Flask app and Debugger instance
app = Flask(__name__)
debugger = Debugger()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/load_snapshot", methods=["POST"])
def load_snapshot():
    snapshot_index = request.json.get("index")
    print(f"Requested snapshot index: {snapshot_index}")  # Debugging print
    try:
        snapshot = debugger.load_snapshot(snapshot_index) 
        print(f"Loaded snapshot: {snapshot}")  # Debugging print
        response = {
            "status": "success",
            "snapshot": {
                "filename": snapshot["filename"],
                "line_number": snapshot["line_number"],
                "local_variables": snapshot["local_variables"],
            }
        }
    except IndexError:
        response = {"status": "error", "message": "Snapshot not found."}
        print("Snapshot not found!")
    return jsonify(response)

def test_function():
    a = 1
    b = 2
    c = a + b +b
    return c

if __name__ == "__main__":
    debugger.start_debugging(test_function)
    app.run(debug=True)
