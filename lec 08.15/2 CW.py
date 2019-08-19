def absolut(number):
    """This func search the absolut of the numb"""
    number *=-1
    if number >0:
        return number
    elif number==0:
        return 0
    else:
        return absolut(number)

numb = int(input("Write the number: "))
ress = str(absolut(numb))
print("Absolut number of {} is: ".format(numb) + ress)
