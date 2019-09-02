try:
    number_list = (2,3,4,5,7,12,14,23)
    number_list = list(number_list)
    for i in range(len(number_list)):
        number_list[i]=float(number_list[i])
        i+=1
    print(str(number_list))
except IndexError as ind:
    print(ind)
except:
    print("booo!")