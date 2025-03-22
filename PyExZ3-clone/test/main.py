def example_function(x):
    assert isinstance(x, int), "x must be an integer"
    return x * 2

def min_function(a, b):
    assert isinstance(a, int) and isinstance(b, int), "Both a and b must be integers"
    return a if a < b else b

def main():
    for i in range(10):
        result = example_function(i)
        print("Result:", result)
        assert result != 10, "Result should not be 10"  # Triggering an AssertionError

def expected_result():
    return None

if __name__ == "__main__":
    main()

