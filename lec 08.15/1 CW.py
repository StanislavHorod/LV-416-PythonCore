def midl_arifmetick(nums): 
    suma = 0 
    num_count = len(nums) 
    midl = 0 
    for i in nums: 
        suma = suma + i 
        midl = suma / num_count 
    return float(midl)


i = 0
numbers = []
counter = int(input("Write the count of numbers: "))

while i<counter:
    numbers.append(int(input("Write number {}: ".format(i+1))))
    i+=1

result_of_look = str(midl_arifmetick(numbers))
print("The midl arifmetic is: " + result_of_look)


