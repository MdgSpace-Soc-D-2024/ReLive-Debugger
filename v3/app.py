from flask import Flask, request, jsonify, send_from_directory
import bdb
import threading
import os
import sys
from io import StringIO

app = Flask(__name__, static_folder='frontend')

debugger_instance = None

def run_code(code, debugger):
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    debugger_output = StringIO()
    
    sys.stdout = debugger_output
    sys.stderr = debugger_output

    try:
        exec(code, {"__name__": "__main__"})
    except Exception as e:
        debugger.set_exception(e)
    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr
        debugger.output = debugger_output.getvalue()
        debugger_output.close()

class WebDebugger(bdb.Bdb):
    def __init__(self):
        super().__init__()
        self.breakpoints = []
        self.stack_frames = []
        self.call_stack = []
        self.variables = {}
        self.exception = None
        self.output = ""  # Store captured output

    def set_exception(self, e):
        self.exception = str(e)


    def user_line(self, frame):
        # Called when the debugger stops at a line
        self.stack_frames.append(self.format_stack_frame(frame))
        self.variables = frame.f_locals

    def format_stack_frame(self, frame):
        # Format stack frame for easy inspection
        return {
            "file": frame.f_code.co_filename,
            "line": frame.f_lineno,
            "function": frame.f_code.co_name,
        }

@app.route("/")
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/start", methods=["POST"])
def start_debugger():
    global debugger_instance
    code = request.json.get("code")

    if not code:
        return jsonify({"error": "No code provided"}), 400

    debugger_instance = WebDebugger()
    threading.Thread(target=run_code, args=(code, debugger_instance)).start()

    return jsonify({"message": "Debugger started"})

@app.route("/breakpoints", methods=["POST"])
def set_breakpoints():
    global debugger_instance
    if not debugger_instance:
        return jsonify({"error": "Debugger not running"}), 400

    breakpoints = request.json.get("breakpoints", [])
    for bp in breakpoints:
        debugger_instance.set_break(bp["file"], bp["line"])
    
    return jsonify({"message": "Breakpoints set", "breakpoints": breakpoints})

@app.route("/status", methods=["GET"])
def get_status():
    global debugger_instance
    if not debugger_instance:
        return jsonify({"error": "Debugger not running"}), 400

    status = {
        "stack_frames": debugger_instance.stack_frames,
        "variables": debugger_instance.variables,
        "exception": debugger_instance.exception,
        "output": debugger_instance.output,  # Add output
    }

    return jsonify(status)


@app.route("/control", methods=["POST"])
def control_execution():
    global debugger_instance
    if not debugger_instance:
        return jsonify({"error": "Debugger not running"}), 400

    action = request.json.get("action")
    
    if action == "step":
        debugger_instance.set_step()
    elif action == "continue":
        debugger_instance.set_continue()
    elif action == "quit":
        debugger_instance.set_quit()
    else:
        return jsonify({"error": "Invalid action"}), 400

    return jsonify({"message": f"Action '{action}' performed"})

if __name__ == "__main__":
    app.run(debug=True)
