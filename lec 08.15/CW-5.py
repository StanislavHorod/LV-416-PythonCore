def summa_of_numbers(number):
    """this func for looking summa of the numbers"""
    result = 0
    while number > 0:
        result += number % 10
        number //= 10
    return result

test_number = int(input("Write the number: "))
result_summa = summa_of_numbers(test_number)
print("Summa of the numbers {} is {}".format(test_number, result_summa))