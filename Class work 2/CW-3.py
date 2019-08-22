import math

def triangle(height, a_side):
    """func for S of the triangle"""
    return 0.5*height*a_side
def round(radius):
    """func for S of the round"""
    return math.pi*pow(radius, 2)
def choise(chose):
    """this func for choise what do we must to find"""
    print("\n\nFor exit write 3 ")
    if chose == 1:
        h_loc = float(input("Write height of triangle: "))
        a_loc = float(input("Write the lenght of the side: "))
        res = triangle(height= h_loc, a_side = a_loc)
        print("The S of the triangle with height {} and lenght of the side {} is: {}".format(h_loc, a_loc, res))
    elif chose == 2:
        r_loc = float(input("Write radius of round: "))
        res = round(radius= r_loc)
        print("The S of the round with radius {}  is: {}".format(r_loc, res)
        +"\n\n")
    elif chose == 3:
        return 1
    else:
        print("Wrong input, try again")

i=0
while i!=1:
    chalenger = int(input("\nFor find S triangle write 1\nFor find S round write 2\nFor exit write 3\n"))
    i = choise(chalenger)
