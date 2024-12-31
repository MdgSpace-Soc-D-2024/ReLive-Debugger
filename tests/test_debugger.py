import unittest
from app.debugger import Debugger

class TestDebugger(unittest.TestCase):
    def test_snapshot_creation(self):
        debugger = Debugger()
        def sample_function():
            x = 10
            y = 20
            return x + y
        debugger.start_debugging(sample_function)
        self.assertTrue(len(debugger.snapshots) > 0)
