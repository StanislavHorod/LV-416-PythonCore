pairs = []
nonpairs = []
special = []
for i in range(10):
    if i%2==0:
        pairs.append(i)
    elif i%3==0 and i%2!=0:
        nonpairs.append(i)
    elif i%3!=0 and i%2!=0:
        special.append(i)
print("Pairs that division on 2 is: " + str(pairs)+
    "\nNonpairs that division on 3 is: " + str(nonpairs)+
    "\nThe special numbers that not divion on 2 and 3: " + str(special))
