class CustomExaption(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)

days = {
    1: "focus: Mondey",
    2: "focus: Tuesday",
    3: "focus: Wednesday",
    4: "focus: Thursday",
    5: "focus: Friday",
    6: "focus: Saturday",
    7: "focus: Sunday"
}
while True:
    try:
        chooser = int(input("Write the number for focus (1-7): "))
    #     if chooser==1:
    #         print("focus: Mondey")
    #         break
    #     elif chooser==2:
    #         print("focus: Tuesday")
    #         break
    #     elif chooser==3:
    #         print("focus: Wednesday")
    #         break
    #     elif chooser==4:
    #         print("focus: Thursday")
    #         break
    #     elif chooser==5:
    #         print("focus: Friday")
    #         break
    #     elif chooser==6:
    #         print("focus: Saturday")
    #         break
    #     elif chooser==7:
    #         print("Sunday")
    #         break
    #     elif chooser>7 or chooser<1:
    #         raise CustomExaption("Ooops, you write the wrong number {}!".format(chooser))
    # except ValueError:
    #     print("Wrong input")
    # except CustomExaption as exi:
    #     print(exi.data)
    except ValueError:
        print("Ooops, you write not number ")
    else:
        print(days.get(chooser, "There is no such day!"))
        