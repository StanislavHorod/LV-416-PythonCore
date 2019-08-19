counter = int(input("Write count of numbers: "))
number_list = []

for i in range(counter):
    number_list.append(int(input("Write {} number: \n".format(i+1))))
maxi= str(max(number_list))
mini = str(min(number_list))
print("Maximum of numbers is: "+ maxi +"\nMinimum of numbers is: " + mini)