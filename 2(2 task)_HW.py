numb = int(input("Write 4-letters number: "))
mus = []
mus.append(numb//1000)
mus.append((numb % 1000) //100)  
mus.append((numb % 100) //10)
mus.append(numb % 10)
multi = 1
for i in range(4):
    multi *=mus[i]

multi = str(multi)

for i in range(4):
    revers += str(mus[i])

for i in range(4):
    for j in range(4-i-1):
        cash = 0
        if mus[j] > mus[j+1]:
            cash = mus[j+1]
            mus[j+1] = mus[j]
            mus[j] = cash
sort = str(mus[0])+str(mus[1])+str(mus[2])+str(mus[3])

print("Results :\n 1) Multiplication - " +  multi +
     "\n 2) Revers - " + revers + "\n 3) Sorting - "+
     sort )