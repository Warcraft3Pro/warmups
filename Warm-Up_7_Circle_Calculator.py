"""
Filename: Warm-Up_7_Circle_Calculator.py
Author: <Daniels, Elias>
Created: <12/04/2025>
Instructor: Holtslander
"""

def circle_calculator():
    """
    Calculates the area and circumference of a circle.
    Asks the user to enter the radius of the circle.
    Uses the formulas
    A = pi*r**2
    C = 2*pi*r
    :return: None
    """
    ### YOUR CODE GOES HERE ###
    r = float(input('What is the radius of your circle?\n'))
    print("Your area is", 3.14*r**2)
    print(f"Your circumference is {2*3.14*r}")

### YOU SHOULD NOT NEED TO CHANGE ANYTHING HERE ###
if __name__ == '__main__':

    circle_calculator()

