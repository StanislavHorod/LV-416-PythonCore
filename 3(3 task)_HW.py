number = int(input("Write the number: "))
start_number = str(number)
cash = 1
while number>1:
    cash *=number
    number-=1
final_number = str(cash)
print("The factorial of the "+start_number+ " is: '"+ final_number)