import sys

def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 != 0

def main():
    def test_is_even():
        assert is_even(2) == True
        assert is_even(3) == False
        assert is_even(0) == True
        assert is_even(-2) == True
        assert is_even(-3) == False

    def test_is_odd():
        assert is_odd(2) == False
        assert is_odd(3) == True
        assert is_odd(0) == False
        assert is_odd(-2) == False
        assert is_odd(-3) == True

    test_is_even()
    test_is_odd()

    num = int(input("Enter a number: "))
    if is_even(num):
        print("The number is even.")
    elif is_odd(num):
        print("The number is odd.")
    else:
        # This part of the code is dead because every integer is either even or odd,
        # so this condition will never be reached.
        print("This will never be printed.")

    print("All tests passed successfully!")

if __name__ == "__main__":
    main()

