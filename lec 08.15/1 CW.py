try:
    def midl_arifmetick(nums): 
        suma = 0 
        num_count = len(nums) 
        midl = 0 
        for i in nums: 
            suma = suma + i 
            midl = suma / num_count 
        return float(midl)
except ZeroDivisionError:
    print("Nums count cant equal 0")


i = 0
numbers = []
try:
    counter = int(input("Write the count of numbers: "))


    while i<counter:
        numbers.append(int(input("Write number {}: ".format(i+1))))
        i+=1
except ValueError:
    print("Write the numbers, not the letters!")
except IndexError as ind:
    print(ind)
    
result_of_look = str(midl_arifmetick(numbers))
print("The midl arifmetic is: " + result_of_look)


