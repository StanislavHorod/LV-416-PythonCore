def absolut(number):
    """This func search the absolut of the numb"""
    number *=-1
    if number >0:
        return number
    elif number==0:
        return 0
    else:
        return absolut(number)
try:
    numb = int(input("Write the number: "))
except ValueError:
    print("write number")
    
ress = str(absolut(numb))
print("Absolut number of {} is: ".format(numb) + ress)
