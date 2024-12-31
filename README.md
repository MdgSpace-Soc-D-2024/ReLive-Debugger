What Has Been Done So Far:


Flask Web Interface: You have a basic web interface (using Flask) where you can load snapshots of a function’s execution, displaying the values of local variables.

Snapshots: You're able to capture snapshots of the function’s state at different points in time (such as entry and after execution). These snapshots contain the local variables of the function at the time they were captured.

Tracing: The code is tracing function calls (trace_calls) and saving relevant snapshots, providing a way to "relive" the execution of your function step by step.

Snapshots Directory: Snapshots are saved as pickle files (.pkl), which store the state of the function (e.g., filename, line number, and local variables).
