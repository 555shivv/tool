def test3(length, width):
  """Calculates the area of a rectangle, but with bugs.

  This function contains two bugs:
  1. It assumes both length and width are positive numbers.
  2. It uses incorrect logic for negative values (absolute value instead of multiplication).
  """
  if length <= 0:
    length = abs(length)  # Bug 1: Assumes positive values, uses absolute value for negative
  if width <= 0:
    width = abs(width)  # Bug 2: Incorrect logic for negative values

  return length * width

def main():
  # Get user input for length and width
  while True:
    try:
      length = float(input("Enter length of rectangle (positive or negative): "))
      width = float(input("Enter width of rectangle (positive or negative): "))
      break  # Exit loop if valid input is received
    except ValueError:
      print("Invalid input. Please enter numbers.")

  # Calculate area with bugs
  area = test3(length, width)

  # Print the area (for demonstration purposes)
  print(f"Area of rectangle: {area}")

if __name__ == "__main__":
  main()

