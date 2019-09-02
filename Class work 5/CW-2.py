def Age(age):
    if age%2==0:
        print("The age {} is paired number".format(age))
    elif age%2==1:
        print("The age {} is not paired number".format(age))
    # try:
    #     age = int(input("Write your age: "))
    #     if age <= 0:
    #         raise Exception("Age cant be negative or equal 0!")
    #     if age%2==0:
    #         print("The age {} is paired number".format(age))
    #     elif age%2==1:
    #         print("The age {} is not paired number".format(age))
    # except ValueError:
    #     print("Wrong input")
    # except Exception as zero:
    #     print(zero)

try:
    inpput_age = int(input("Write your age: "))
    if inpput_age <= 0:
        raise Exception("Age cant be negative or equal 0!")
    Age(inpput_age)
except ValueError:
    print("Wrong input")
except Exception as zero:
    print(zero)