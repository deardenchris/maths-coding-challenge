
# Maths coding challenge!

# 1) Ask user to enter an integer and store as a variable
#    Bonus points for checking that the input is an integer and raise an exception if not!

value = input("Please Enter An Integer: ")
value = int(value)

# 2) Write functions to calculate the square, cube, square root and reciprocal for the given integer

# For example: 

def calc_square(value):
   return value * value

def calc_cube(value):
   return value * value * value
   
# 3) Call each function by passing the integer variable to each 

# For example:

square = calc_square(value)
cube = calc_cube(value)

# 4) print the results to screen

print('Square of', value, 'is :', square)
print('Cube of', value, 'is :', cube)
