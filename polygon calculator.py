
##################################
#Olamide Afolabi
#Polygoncalculator.py
#DATA VIS EDIT FOR HW 1
#09/06/2025
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

