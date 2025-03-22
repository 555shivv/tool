import afl
import sys

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def is_odd(num):
    if num % 2 != 0:
        return True
    else:
        return False

def main():
    afl.init()
    num = int(input("Enter a number: "))
    if is_even(num):
        print("The number is even.")
    elif is_odd(num):
        print("The number is odd.")
    else:
        # This part of the code is dead because every integer is either even or odd,
        # so this condition will never be reached.
        print("This will never be printed.")

if __name__ == "__main__":
    main()

