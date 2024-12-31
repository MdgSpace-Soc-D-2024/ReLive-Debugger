import sys
import pickle
import os
from app.recorder import Recorder

class Debugger:
    def __init__(self):
        self.recorder = Recorder()
        self.snapshots = []
        self.snapshot_dir = os.path.join(os.getcwd(), "snapshots")  # Ensure it's absolute
        os.makedirs(self.snapshot_dir, exist_ok=True)
        self.load_snapshots_from_disk()  # Load any existing snapshots at startup
    
    
    def save_snapshot(self, frame):
        """Save a snapshot of the current frame."""
        # Extract relevant information from the frame
        snapshot_data = {
            "filename": frame.f_code.co_filename,
            "line_number": frame.f_lineno,
            "local_variables": self.clean_locals(frame.f_locals),  # Clean locals before saving
        }

        snapshot_filename = f"snapshot_{len(self.snapshots)}.pkl"
        snapshot_path = os.path.join(self.snapshot_dir, snapshot_filename)
        
        # Save the snapshot data to a file
        with open(snapshot_path, "wb") as f:
            pickle.dump(snapshot_data, f)
        
        self.snapshots.append(snapshot_path)

    def clean_locals(self, locals_dict):
        """Filter out non-pickleable items (e.g., file handles)."""
        clean_dict = {}
        for key, value in locals_dict.items():
            try:
                pickle.dumps(value)  # Try to pickle the value
                clean_dict[key] = value
            except (TypeError, pickle.PicklingError):
                clean_dict[key] = None  # Set non-pickleable items to None or remove them
        return clean_dict
    
    
    def load_snapshots_from_disk(self):
        """Load snapshots from the snapshot directory."""
        snapshot_files = os.listdir(self.snapshot_dir)
        for file in snapshot_files:
            if file.endswith(".pkl"):  # Ensure we're only reading .pkl files
                self.snapshots.append(os.path.join(self.snapshot_dir, file))
    
    def trace_calls(self, frame, event, arg):
        """Trace function calls and line executions."""
        if event == "call" or event == "line":
            self.save_snapshot(frame)  # Capture snapshot on each line or function call.
            self.recorder.record(frame)  # Optionally record the frame for further analysis.
        return self.trace_calls

    def start_debugging(self, file_path):
        """Execute the entire Python file and trace its execution."""
        with open(file_path, "r") as file:
            code = file.read()

        sys.settrace(self.trace_calls)  # Start tracing

        # Execute the Python code in the file
        exec(code, globals(), locals())

        sys.settrace(None)  # Stop tracing after execution is complete
        print("Execution complete.")

    def load_snapshot(self, index):
        """Load a snapshot by its index."""
        print(f"Attempting to load snapshot at index: {index}")  # Debugging print
        try:
            if index < 0 or index >= len(self.snapshots):
                raise IndexError("Snapshot index is out of range.")

            snapshot_path = self.snapshots[index]
            print(f"Snapshot path: {snapshot_path}")  # Debugging print

            with open(snapshot_path, "rb") as f:
                snapshot_data = pickle.load(f)

            print(f"Successfully loaded snapshot: {snapshot_data}")  # Debugging print
            return snapshot_data

        except Exception as e:
            print(f"Error in load_snapshot: {e}")  # Debugging print
            raise


