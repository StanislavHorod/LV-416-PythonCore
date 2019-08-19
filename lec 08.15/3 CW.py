def maximus(firs_number, second_number):
    """This func is searcher of Maximum number, between the 2"""
    if firs_number==second_number:
        print("The {} and {} is equal".format(firs_number, second_number))
    elif firs_number>second_number:
        print("The {} is Maximum".format(firs_number))
    elif second_number>firs_number:
        print("The {} is Maximum".format(second_number))

first = int(input("Write the first numbeer: "))
second = int(input("Write the second numbeer: "))
maximus(firs_number=first, second_number=second)