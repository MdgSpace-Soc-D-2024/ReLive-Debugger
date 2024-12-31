import inspect

class Recorder:
    def record(self, frame):
        stack = inspect.stack()
        current_frame = stack[0]
        local_vars = frame.f_locals
        print(f"Recording frame: {current_frame}")
        print(f"Local variables: {local_vars}")
