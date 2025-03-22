def test0(x):
    assert x > 99, "x must be greater than 0"
    return x * 2

if __name__ == "__main__":
    x = int(input("Enter the value of x: "))

    # Assertion: x should be greater than 0
    print("Result of test_assertion:", test0(x))

