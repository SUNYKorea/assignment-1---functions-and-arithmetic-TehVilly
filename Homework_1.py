# Name: Minseo Kim
# SBUID: 114665786

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

#Input function as well

def fahrenheit2celsius(fahrenheit): 
   celsius = 5/9 * (fahrenheit - 32)
   return celsius

fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
celsius = fahrenheit2celsius(fahrenheit)

def what_to_wear(celsius):
   if celsius < -10:
      print("wear a puffy jacket.")
   elif -10 <= celsius < 0:
      print("wear a scarf.")
   elif 0 <= celsius < 10:
      print("wear a sweater.")
   elif 10 <= celsius < 20:
      print("wear a light jacket.")
   else:
      print("wear a t-shirt.")

what_to_wear(celsius)
# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

import math
#importing math to use math.sqrt
# area of A from its vertex coords using shoelace formula
def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2
    return area


def euclidean_distance(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    side1 = euclidean_distance(x1, y1, x2, y2)
    side2 = euclidean_distance(x2, y2, x3, y3)
    side3 = euclidean_distance(x3, y3, x1, y1)
    perimeter = side1 + side2 + side3
    return perimeter


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

import math
#importing math to use math.pi
def deg2rad(deg):
    return deg * math.pi / 180.0

#theta for deg2rad 
def apothem(number_sides, length_side):
    theta = deg2rad(360 / (2 * number_sides))
    return length_side / (2 * math.tan(theta))

#apothem_length taken from the question #2

def polygon_area(number_sides, length_side):
   perimeter = number_sides * length_side
   apothem_length = apothem(number_sides, length_side)
   return 0.5 * perimeter * apothem_length







# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.



#honestly i didnt notice this section and i thought my code was bugged since it was printing the results twice. makes sense now. :p
#i added the input func for the first question before i saw this so ill just leave the input func up there 



# Exercise 1 test
#fahrenheit = 40
#what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
#x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
#area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
#perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
#print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
#number_sides = 9
#length_side = 10
#print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

