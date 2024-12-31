import sys
import pickle
import os
from app.recorder import Recorder

class Debugger:
    def __init__(self):
        self.recorder = Recorder()
        self.snapshots = []
        self.snapshot_dir = "snapshots"
        os.makedirs(self.snapshot_dir, exist_ok=True)

    def trace_calls(self, frame, event, arg):
        if event == "call":
            self.save_snapshot(frame)  # Save a snapshot of the current frame.
            self.recorder.record(frame)
        elif event == "return":
            # Capture snapshot after the function returns (after execution)
            self.save_snapshot(frame)
        return self.trace_calls

    def start_debugging(self, target_function, *args, **kwargs):
        sys.settrace(self.trace_calls)
        try:
            result = target_function(*args, **kwargs)
        finally:
            sys.settrace(None)
        return result

    def save_snapshot(self, frame):
        # Extract relevant information from the frame
        snapshot_data = {
            "filename": frame.f_code.co_filename,
            "line_number": frame.f_lineno,
            "local_variables": dict(frame.f_locals) 
        }
        snapshot_path = f"snapshots/snapshot_{len(self.snapshots)}.pkl"
        # Save the snapshot data to a file
        with open(snapshot_path, "wb") as f:
            pickle.dump(snapshot_data, f)
        self.snapshots.append(snapshot_path)
        print(f"Snapshot saved: {snapshot_path}")
        print(f"Snapshots list: {self.snapshots}")

    def load_snapshot(self, index):
        if index < 0 or index >= len(self.snapshots):
            raise IndexError("Snapshot index out of range.")
        snapshot_path = self.snapshots[index]
        with open(snapshot_path, "rb") as f:
            snapshot_data = pickle.load(f)
        return snapshot_data


