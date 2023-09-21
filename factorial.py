"""Factorial Module"""


class Factorial:
    """Class for solving Factorial"""

    def solve(self, number):
        """Method to solve factorial given a number"""

        # This is the base case
        # If the number is 1, return 1.
        # Without this base case, there will be a ?????
        if number == 1:
            return number

        # Not the base case, so make a recursive call to ourself.
        right_part = self.solve(number - 1)
        return number * right_part

        # factorial.solve(number) = return 5 * self.solve(5 - 1)
        # return 5 * self.solve(5 - 1)
        # return 5 * (4 * self.solve(4 - 1))
        # return 5 * (4 * (3 * self.solve(3 - 1)))
        # return 5 * (4 * (3 * (2 * self.solve(2 - 1))))
        # return 5 * (4 * (3 * (2 * (1))))
