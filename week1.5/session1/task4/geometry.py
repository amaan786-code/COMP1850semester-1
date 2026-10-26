# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!
class Point:
    """
    A Point in 2D space.
    """
    def __init__(self, x, y):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x
        self.y = y
        
    def distance(self):
        return math.hypot(self.x, self.y)
    
    def distance_to(self, point):
        """
        Returns distance from this point to the specified point
        """
        return math.hypot(self.x - point.x, self.y - point.y)

class Circle:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius
        
    def area(self):
        return(math.pi * self.radius**2)
    
    def perimeter(self):
        return(2 * math.pi * self.radius)
        
        