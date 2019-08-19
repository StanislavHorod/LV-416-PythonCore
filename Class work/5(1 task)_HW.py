print("The pair number is \nVariant 'while'\n\n")
i=0
while i<100:
    if i%2==0:
        print(str(i)+"\n")
    i+=1

print("The pair number is \nVariant 'for'\n\n")

for j in range(0,100, 2):
    print(str(j)+"\n")
    j+=1