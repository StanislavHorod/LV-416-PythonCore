try:
    test_number = int(input("Write number for test: "))
    if test_number%2==0:
        print("The number {} is paired".format(test_number))
    elif test_number%2==1:
        print("The number {} is not paired".format(test_number))
except ValueError:
    print("Wrong input")