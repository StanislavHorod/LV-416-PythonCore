def funk_parser(number):
    
    a, b = 0 , 0
    result_set = []
    result_set.append(number.split())
    for i in range(len(result_set)):
        if type(result_set[i])!=int:
            print("error!")

        elif result_set[i]%2==1:
            a +=1
        elif result_set[i]%2==0:
            b+=1
        
        
    some_dict = {"odd": a, "even": b}
    return some_dict



