def square(wi_param, hi_param):
    """This func for square """
    return wi_param*hi_param
def triangle(a_side, b_side, c_side):
    """This funck for triangl"""
    hulf_perim = (a_side + b_side + c_side)/2
    S = (hulf_perim*(hulf_perim-a_side)*(hulf_perim-b_side)*(hulf_perim-c_side))**0.5
    return S
def round(radius):
    """This func for radius"""
    return 3.14*(radius**2)

choise = input("Choose the figure:\nSquare-1\nTriangle-2\nRound-3")
if choise == 1:
    w_param = int(input("Write width: "))
    h_param = int(input("Write hidth: "))
    rest = square(w_param, h_param)

elif choise == 2:
    a_param = int(input("Write a-side: "))
    b_param = int(input("Write b-side: "))
    c_param = int(input("Write c-side: "))
    rest = triangle(a_param, b_param, c_param)
    print
elif choise == 3:
    r_param = int(input("Write radius: "))
    rest = round(r_param)

