test_number = int(input("Write number for test: "))
caunt = 0
for i in range(test_number):
    if test_number%(i+1)==0:
        caunt+=1
        i+=1
    else:
        i+=1
    if caunt > 2:
        print("The number is composite")
        break
    elif i==test_number and caunt == 2:
        print("The number is not composite")
    