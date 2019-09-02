try:
    login = input("Press login: ")
    while True:
        if login == "First":
            print("Gracios, you are connected")
            break
        elif login == " ":
            raise Exception("Write login!")
        else:
            login = input("Try again\nPress login: ")
except Exception as exi:
    print(exi)