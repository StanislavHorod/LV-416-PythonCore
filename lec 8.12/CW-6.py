try:    
    count = int(input("Write count of numbers: "))
    number_list = []
except ValueError:
    print("write count by numbers")
try:
    for i in range(count):
        cash = int(input("Write number: "))
        if cash < 0:
            print("There is number with minus")
            break
        else:
            number_list.append(cash)
except ValueError:
    print("write numbers by number, not by letters")