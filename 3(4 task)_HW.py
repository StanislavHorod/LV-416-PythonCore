firs_number = int(input("Write first number: "))
second_number = int(input("Write second number: "))
points_of_1_part = []
maximus = max(firs_number, second_number)
for i in range(1, maximus):
    if firs_number%i==0 and second_number%i==0:
        points_of_1_part.append(i)

msd = max(points_of_1_part)
msk = str(int((firs_number*second_number)/msd))
msd = str(msd)
print("The MSD of the %s and %s is: "%(firs_number, second_number)  + msd
    + "\nThe MSK of the %s and %s is: "%(firs_number, second_number) + msk)