
##################################
#Olamide Afolabi
#Polygoncalculator.py
#In this project, you will create a method called calcPolygon() that will accept two numbers as a parameters which are the number of sides of the polygon and the length of one of the sides. The method will return a number that is the area of the polygon. The method will calculate the area in square feet of the polygon using the formula:
#04/28/2020
#################################



import math
def calcPolygon(num_sides,length):
    
    area=(num_sides*length**2)/(4*math.tan(math.pi/num_sides))
    return area

def main():
    
    n=int(input("Enter the number of sides of the polygon: "))
    s=float(input("Enter the length of a side: "))
   
    area=calcPolygon(n,s)
    
    print("The area of the polygon is: {:.2f}".format(area))



main()

