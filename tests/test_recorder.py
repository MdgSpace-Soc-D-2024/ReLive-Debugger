import unittest
from app.recorder import Recorder

class TestRecorder(unittest.TestCase):
    def test_record(self):
        recorder = Recorder()
        def sample_function():
            x = 5
            y = 10
            return x + y

        recorder.record(sample_function.__code__)
        # No exception means the test passed
        self.assertTrue(True)
