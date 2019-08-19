end_point = int(input("Write end-point for Fiboo: "))
fib_numb_1 = 1
fib_numb_2 = 1
if end_point<2:
    print("\nResult: 1")
    
else:
    print(str(fib_numb_1) + " " + str(fib_numb_2) + " ")
    for i in range(2, end_point):
        fib_sum = fib_numb_1 + fib_numb_2
        fib_numb_1 = fib_numb_2
        fib_numb_2 = fib_sum
        i=i+1
        print(str(fib_numb_2) + " ")
