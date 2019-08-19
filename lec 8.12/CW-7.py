FibArray = [0,1] 
def fibonachu(number):
    """fibonachi recursiv"""
    if number<=0:
        print("Write positiv number: ")
    elif number<=len(FibArray):
        return FibArray[number-1]
    else:
        temp_fib = fibonachu(number-1)+fibonachu(number-2) 
        FibArray.append(temp_fib) 
        return temp_fib 
            
 
counter = int(input("Write for what number fibo we must work: "))
for i in range(counter+2):
    print(fibonachu(i))

