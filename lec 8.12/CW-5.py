try:
    number = int(input("Press number: "))
    while True:
        if number == 0 or int(number) < 0:
            print("There is number with minus: " + number)
            break
        else:
            number = input("Try again\nPress number: ")
except ValueError:
    print("write numbers")
        