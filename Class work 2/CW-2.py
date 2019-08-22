from Random import random

cell = random(0, 1000)
i = 1
uzver = int(input("Write number: "))
while i!=0:
    if uzver == cell:
        print("Congrat you right!")
        i = 0
    else:
        uzver = int(input("Try again\nWrite number: "))