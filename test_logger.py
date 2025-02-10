from dramatic_logger.DramaticLogger import DramaticLogger
import threading
import time

# This is a test script to test the DramaticLogger.
# It will test the logger with various scenarios and stress tests.

DELAY = 0.1  # 100ms delay between log messages

def simulate_error():
    try:
        raise ValueError("Test error")
    except Exception as e:
        # This should trigger the same error you're seeing
        DramaticLogger["Dramatic"]["error"]("Test error message", exc_info=True)
        time.sleep(DELAY)

def test_various_scenarios():
    # Test normal message
    DramaticLogger["Dramatic"]["info"]("Normal message")
    time.sleep(DELAY)
    
    # Test with details
    DramaticLogger["Dramatic"]["warning"]("Warning message", "Additional details")
    time.sleep(DELAY)
    
    # Test with exc_info
    simulate_error()
    time.sleep(DELAY)
    
    # Test with other kwargs
    DramaticLogger["Dramatic"]["debug"]("Debug message", stacklevel=2)
    time.sleep(DELAY)
    
    # Test with invalid input
    DramaticLogger["Dramatic"]["error"](None, exc_info=True)
    time.sleep(DELAY)
    
    # Test with complex object
    DramaticLogger["Dramatic"]["info"]({"complex": "object"})
    time.sleep(DELAY)

def stress_test_logger():
    """Attempt to break the logger with various edge cases and stress tests"""
    
    # Test extremely long messages
    DramaticLogger["Dramatic"]["info"]("x" * 1000)
    time.sleep(DELAY)
    DramaticLogger["Dramatic"]["error"]("x" * 10000, "y" * 10000)
    time.sleep(DELAY)
    
    # Test special characters and Unicode
    DramaticLogger["Dramatic"]["info"]("🔥 Unicode 🚀 Test ® © ™ 漢字 🌈")
    time.sleep(DELAY)
    DramaticLogger["Dramatic"]["warning"]("Line1\nLine2\nLine3\n\n\nMany\nNew\nLines")
    time.sleep(DELAY)
    
    # Test various Python objects
    DramaticLogger["Dramatic"]["debug"](Exception("Test Exception"))
    time.sleep(DELAY)
    DramaticLogger["Dramatic"]["error"](TypeError())
    time.sleep(DELAY)
    DramaticLogger["Dramatic"]["info"](object())
    time.sleep(DELAY)
    DramaticLogger["Dramatic"]["warning"]([1, 2, 3, {"nested": "object"}])
    time.sleep(DELAY)
    
    # Test invalid/edge case inputs
    DramaticLogger["Dramatic"]["error"](None)
    time.sleep(DELAY)
    DramaticLogger["Dramatic"]["warning"]("")
    time.sleep(DELAY)
    DramaticLogger["Dramatic"]["info"](False)
    time.sleep(DELAY)
    DramaticLogger["Dramatic"]["debug"](0)
    time.sleep(DELAY)
    
    # Test with various kwargs combinations
    DramaticLogger["Dramatic"]["error"]("Test", exc_info=True, extra={"custom": "data"})
    time.sleep(DELAY)
    DramaticLogger["Dramatic"]["warning"]("Test", stacklevel=999)
    time.sleep(DELAY)
    DramaticLogger["Dramatic"]["info"]("Test", enqueue=True, catch=True, colorize=True)
    time.sleep(DELAY)
    
    # Test nested exceptions
    try:
        try:
            raise ValueError("Inner error")
        except ValueError as e:
            raise RuntimeError("Outer error") from e
    except Exception as e:
        DramaticLogger["Dramatic"]["error"]("Nested exception test", exc_info=True)
        time.sleep(DELAY)
    
    # Test concurrent logging (no delay here to test concurrency)
    def concurrent_log():
        for i in range(100):
            DramaticLogger["Dramatic"]["info"](f"Concurrent message {i}")
            DramaticLogger["Normal"]["debug"](f"Normal concurrent message {i}")
    
    print("\nStarting concurrent logging test...")
    threads = [threading.Thread(target=concurrent_log) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    time.sleep(DELAY * 2)  # Longer pause after concurrent test
    
    # Test rapid-fire logging (reduced count and added small delay)
    print("\nStarting rapid-fire test...")
    for i in range(50):  # Reduced from 1000 to 50
        DramaticLogger["Dramatic"]["debug"](f"Rapid message {i}")
        time.sleep(DELAY/10)  # Very small delay to make it readable but still quick
    time.sleep(DELAY)
    
    # Test alternating between Normal and Dramatic
    print("\nStarting alternating test...")
    for i in range(20):  # Reduced from 100 to 20
        logger_type = "Dramatic" if i % 2 == 0 else "Normal"
        level = ["info", "warning", "error", "critical", "debug"][i % 5]
        DramaticLogger[logger_type][level](f"Alternating message {i}")
        time.sleep(DELAY/2)
    
    # Test with various combinations of details and kwargs
    print("\nTesting various combinations...")
    test_cases = [
        ("Message", None, {}),
        ("Message", "Details", {}),
        ("Message", None, {"exc_info": True}),
        ("Message", "Details", {"exc_info": True}),
        ("", "", {"stacklevel": 2}),
        (None, None, {"exc_info": True}),
        ("Message", Exception("Test"), {}),
        (Exception("Test"), "Details", {"exc_info": True}),
    ]
    
    for msg, details, kwargs in test_cases:
        try:
            DramaticLogger["Dramatic"]["error"](msg, details, **kwargs)
            DramaticLogger["Normal"]["error"](msg, details, **kwargs)
            time.sleep(DELAY)
        except Exception as e:
            DramaticLogger["Dramatic"]["critical"](f"Test case failed: {msg}, {details}, {kwargs}", exc_info=True)
            time.sleep(DELAY)

if __name__ == "__main__":
    print("Running basic scenarios...")
    test_various_scenarios()
    
    print("\nRunning stress tests...")
    stress_test_logger()
    
    print("\nTests completed!") 