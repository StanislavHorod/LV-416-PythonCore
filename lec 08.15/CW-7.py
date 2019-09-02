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
            
try: 
    counter = int(input("Write for what number fibo we must work: "))
except ValueError:
    print("write numbers not letter")
    
for i in range(counter+2):
    print(fibonachu(i))

