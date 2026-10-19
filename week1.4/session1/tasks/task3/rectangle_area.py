
# function implementation
"""
def rectangle_area(length, height ):  # define suitable input data

    if length == height:
        print("Only enter the measurments of the rectangle")
    else:
        area = length * height
                        # implement the function
        return area            # return an appropriate value
        
# testing the function
length = int(input("Enter a the length of the rectangle: "))
height = int(input("Enter the height of the rectangle: "))
print(f"Area is {rectangle_area(length, height )}")   # provide suitable data matching your inputs
"""
def even_numbers(limit):
    evens = []
    for n in range(limit + 1):
        if n % 2 == 0:
            evens.append(n)
    return evens

print(even_numbers(20))
