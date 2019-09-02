try:
    a = int(input("write 1 number: "))
    b = int(input("write 2 number: "))

    print("result of a+b is: " + str(a+b) + "\n"
         + "result of a-b is: " + str(a-b) + "\n"
         + "result of a*b is: " + str(a*b) +"\n"
        + "result of a/b is: " + str(a/b))
except ValueError:
     print("write numbers, not letters")