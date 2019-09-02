try:
    for i in (2, 4, 6, 7, 9):
        if i%2!=0:
            print("There is non paired number %s"%i)
            break
except:
        print("this text also will newer be printed")
    