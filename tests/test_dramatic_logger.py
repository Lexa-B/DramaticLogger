import unittest
from dramatic_logger import DramaticLogger

class TestDramaticLogger(unittest.TestCase):
    def test_success_log(self):
        try:
            DramaticLogger['Dramatic']['success']("Test success message")
        except Exception as e:
            self.fail(f"Success log raised an exception {e}")

    # Add more tests for other logging levels

if __name__ == '__main__':
    unittest.main()
