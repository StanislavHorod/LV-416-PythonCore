def summa_of_numbers(number):
    """this func for looking summa of the numbers"""
    result = 0
    while number > 0:
        result += number % 10
        number //= 10
    return result
    
try:
    test_number = int(input("Write the number: "))
except ValueError:
    print("write number, not letter")

result_summa = summa_of_numbers(test_number)
print("Summa of the numbers {} is {}".format(test_number, result_summa))