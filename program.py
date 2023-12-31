"""Program code"""

# First-party imports
from factorial import Factorial
from tower_of_hanoi import TowerOfHanoi

def main(*args):
    """Method to run program"""
    # Create instance of Factorial Class to use
    factorial = Factorial()
    hanoi = TowerOfHanoi()

    # Show menu and collect input
    print("Enter 1 for factorial, 2 for Tower of Hanoi, 3 to Exit")
    choice = input()

    # While choice is less than exit criteria.
    # NOTE: Assuming good input from user.
    while int(choice) < 3:
        # If solving Factorial
        if choice == "1":
            # Do Factorial
            print("What number would you like to solve? 5 is a good choice.")
            print("> ", end="")
            number = int(input())

            print()
            print(f"Solving {number}!")
            print("The answer is: ", end="")
            print(factorial.solve(number))

        elif choice == "2":
            # Do Tower of Hanoi
            print("What number of discs would you like to solve? 5 is good.")
            print("> ", end="")
            number = int(input())

            print()
            print(f"Solving {number} discs")
            print("See the steps below.")
            print()
            hanoi.solve(number)

        # Re-show menu and collect input.
        print()
        print()
        print("Enter 1 for factorial, 2 for Tower of Hanoi, 3 to Exit")
        choice = input()
