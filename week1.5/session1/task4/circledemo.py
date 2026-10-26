# Week 1.5, Session 1: Task 4
import math
# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle
class Circle:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius
        
    def area(self):
        return(math.pi * self.radius**2)
    
    def perimeter(self):
        return(2 * math.pi * self.radius)