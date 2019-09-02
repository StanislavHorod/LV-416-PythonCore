try:
    divis = input("Write 2 numbers for division (in form X, Y): ")
    parts = divis.rsplit(',', 1)
    result = int(parts[0])/int(parts[1])
    ## div1, div2 = eval(input("text")) and blablabla
    print("The division of the {} and {} is {}".format(parts[0], parts[1], result))
except ZeroDivisionError:
    print("The 2-nd number is 0!")
except ValueError:
    print("Wrong input")
except:
    print("error!")
else:
    print("Here is else part =(")
finally:
    print("End of the program")