# German Zavala Villafuerte
'''
Triangle Creation
A program that creates a triangle based on the given side values. The program checks to see
if the triangle is valid, and what type of triangle it is. It also caluclates the area, and determines if 
triangle is also a right triangle. 

English Statements
ask the user for three sides of the tirangle, with being positive float numbers
If the user inputs a negative number the program should inform the user and end. 
Use heron formula to determine if the trinagle is valid
caluclate s half of the tirangle perimeter

If the triangle is invalid print all sides, inform user of invalitidy, and end program. 

If the triangle is valid inform user, then
print all sides, calculate and print area. 

Check if triangle is a equilateral, isosceles, or scalene. The print the type. 
If the triangle is an isoceles or scalene then it might be a right triangle. 

find the largest side
then use pathagriumms thereom c**2 = a**2 + b**2 to see if tringale is a right triangle. 
print if it is a right triangle and largest side. 


Psuedo Code
side_one = get value from user, prompt("Enter a positive float number: ")
side_two = get value from user, prompt("Enter a positive float number: ")
side_three = get value from user, prompt("Enter a positive float number: ")

if any of the sides are negative
    print "You entered a negative number, please rerun program and enter only positive numbers."
    End program

calculate s half of the perimeters fomula 
s = (side_one+side_two+side_three)/2


if s or (s-side_one) or (s-side_two) or (s-side_three) equal 0 or less. 
    print "The sides make an invalid formula. Please rerun program and input new side values."
    print all sides
    End Program

caluclate the area
area = square root(s(s-side_one)(s-side_two)(s-side_three))

print all sides
print area

if all sides equal to each other
    print "Your triangle is an equilateral"
elif no side are equal to each other
    print "Your triangle is a Scalene"
else
    print "Your triangle is a isosceles"

if side one is large than side two and side three
    if side one^2 == side two^2 + side three^2
else if side two is large than side two and side three
    if side two^2 == side one^2 + side three^3
else if side three is large than side two and side three
    if side three^2 == side two^2 + side one^3

Testing
Test 1 2/18/24
--------
side_one = 4
side_two = 3
side_three = 5

expected area = 6
actual area = 6
Expected Right Angle
Expected Scalene Triangle
Actual Right Angle and Scalene Triangle

Test 2 2/18/24
--------
side_one = 5
side_two = 10
side_three = 18

expecation print all sides and print error of invalid triangle. 
acutal print all sides and print error of invalid triangle.

Test 3 2/18/24
--------
side_one = -5
side_two = -3
side_three = 6

expected print error of negative number
actual print error of negative number

Test 4 2/18/24
--------
side_one = 6
side_two = 6
side_three = 6

expected area = 15.59
expected equilateral 
actual area = 15.59
actual Equilateral

Test 5 2/18/24
--------
side_one = 6
side_two = 8
side_three = 8

expected area = 22.25
expected isosceles
acutal = 22.25
actual isosceles


Test 6 2/18/24
--------
side_one = 3
side_two = 6
side_three = 4

expected area = 5.33
expected scalene
actual area = 5.33
expected Scalene

'''
import math

# Ask user for values of triangle sides
try: 
    side_one = float(input("Enter a positive float number in inches for triangle side: "))
    side_two = float(input("Enter a positive float number in inches for triangle side: "))
    side_three = float(input("Enter a positive float number in inches for triangle side: "))
except ValueError as message:
    print(f"You did not enter a float number: {message}")
    print(f"We will use the deafault values of 3,4,5. ")
    side_one = 3
    side_two = 4
    side_three = 5
print()

# Checks if sides are negative. If they are end program
if side_one < 0 or side_two < 0 or side_three < 0:
    print("You entered a negative number, please rerun program and enter only positive numbers.")
    exit()

# Calculates s which is half the perimeter of the triangle. 
half_of_perimeter = (side_one + side_two + side_three)/2

# Checks if sides make a valid triangle by using Herons formula. 
if half_of_perimeter <= 0 or (half_of_perimeter-side_one <= 0) or (half_of_perimeter-side_two <= 0) or (half_of_perimeter-side_three <= 0):
    # Does not make a valid triangle end program
    print("The sides make an invalid formula. Please rerun program and input new side values.")
    print(f"Side One: {side_one} in")
    print(f"Side Two: {side_two} in")
    print(f"Side Three: {side_three} in")
    exit()

# Calculates the area of the triangle. 
area = math.sqrt(half_of_perimeter*(half_of_perimeter-side_one)*(half_of_perimeter-side_two)*(half_of_perimeter-side_three))

# Prints the side and area. 
print(f"Side One: {side_one} in")
print(f"Side Two: {side_two} in")
print(f"Side Three: {side_three} in")
print(f"Area of Trianlge: {area:0.2f} inches squared")

# Keeps track of the possibility of the triangle being a right triangle. 
could_be_right_triangle = False

# If all sides are equal than its a Equilateral
if side_one == side_two and side_one == side_three and side_two == side_three:
    print("Your triangle is an Equilateral")
# if all sides are not equal than its a Scalene, and could be a right triangle
elif side_one != side_two and side_one != side_three and side_two != side_three:
    print("Your triangle is a Scalene")
    could_be_right_triangle = True
# Otherwise its an Isosceles and could be a right triangle. 
else:
    print("Your triangle is an Isosceles")
    could_be_right_triangle = True

# If possibility of a right triangle is true.
if could_be_right_triangle:
    # Finds which side is the largest. If no side is larger than its not a right triangle. 
    if side_one > side_two and side_one > side_three:
        # Confirms right triangle using pathagriumns thereom
        if side_one**2 == side_two**2 + side_three**2:
            # Prints hypotenuse length and it is a right triangle. 
            print("Your triangle is a right triangle")
            print(f"Hypotenuse Length: {side_one}")
    elif side_two > side_one and side_two > side_three:
        # Confirms right triangle using pathagriumns thereom
        if side_two**2 == side_one**2 + side_three**2:
            # Prints hypotenuse length and it is a right triangle.
            print("Your triangle is a right triangle")
            print(f"Hypotenuse Length: {side_two}")
    elif side_three > side_one and side_three > side_two:
        # Confirms right triangle using pathagriumns thereom
        if side_three**2 == side_one**2 + side_two**2:
            # Prints hypotenuse length and it is a right triangle.
            print("Your triangle is a right triangle")
            print(f"Hypotenuse Length: {side_three}")





