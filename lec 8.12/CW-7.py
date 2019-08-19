for test_number in range(10, 31):
    i = 2
    base = int(test_number**0.5)
    while i <= base:
        if test_number % i == 0:
            half = test_number/2
            print("Number {} equal 2*{}".format(test_number, half))
            break
        i += 1
    else:
        print("Number {} is easy".format(test_number))