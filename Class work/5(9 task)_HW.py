from random import random
try:
    real_number = str(int(random()*1000000))
    print(real_number)
    number_list = list(real_number)
    maxi = max(number_list)
    if maxi==min(number_list):
        raise Exception("Collapse!")
    print(str(maxi))
except Exception as exi:
    print(exi)