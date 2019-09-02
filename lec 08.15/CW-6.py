def summan(a, b):
    """this func of the summa 2 numbers"""
    return a+b
def diff(a, b):
    """this func for the difference between 2 numbers"""
    return a-b
def multipli(a, b):
    """this func for multiplication of the 2 numbers"""
    return a*b
def div(a, b):
    """this func for division of the a on the b"""
    return a/b
def square(a, b):
    """this func for square a on b"""
    return a**(1/b)
def degree(a, b):
    """this func for finding of the a degree b""" 
    return a**b
try:
    def changer():
        variant= int(input("Greatings\nFor getting summa write 1\nFor getting difference write 2" + 
               "\nFor getting multiplication write 3\nFor getting division write 4"+
               "\nFor getting square write 5\nFor getting degree write 6"+
               "\nFor exit write 7"))
        if variant == 1:
            a = int(input("You choose summa\nWrite first number: "))
            b = int(input("Write second number: "))
            res = str(summan(a=a, b=b))
            print("The resault of the summa between {} and {} is {}".format(a, b, res))
        elif variant == 2:
            a = int(input("You choose different\nWrite first number: "))
            b = int(input("Write second number: "))
            res = str(diff(a=a, b=b))
            print("The resault of the different between {} and {} is {}".format(a, b, res))
        elif variant == 3:
            a = int(input("You choose multiplication\nWrite first number: "))
            b = int(input("Write second number: "))
            res = str(multipli(a=a, b=b))
            print("The resault of the multiplication between {} and {} is {}".format(a, b, res))
        elif variant == 4:
            a = int(input("You choose division\nWrite first number: "))
            b = int(input("Write second number: "))
            res = str(div(a=a, b=b))
            print("The resault of the division between {} and {} is {}".format(a, b, res))
        elif variant == 5:
            a = int(input("You choose square\nWrite first number: "))
            b = int(input("Write degree number: "))
            res = str(div(a=a, b=b))
            print("The resault of the square between {} degree {} is {}".format(a, b, res))
        elif variant == 6:
            a = int(input("You choose degree\nWrite first number: "))
            b = int(input("Write power number: "))
            res = str(div(a=a, b=b))
            print("The resault the degree between {} on {} is {}".format(a, b, res))
        elif variant == 7:
            print("Thanks for using our calculator!")
            return 1
        else:
            raise Exception("wrong choise")
except ValueError:
    print("write numbers, not letters")
except Exception as exi:
    print(exi)
    
i = 0
while i!=1:
    looker = changer()
    if looker == 1:
        i = 1
    
