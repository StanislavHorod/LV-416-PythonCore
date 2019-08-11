test_word = input("Write word for test: ")
leng_of_the_word = len(test_word)

for el in range(leng_of_the_word//2):
    if test_word[el] != test_word[-1-el]:
        print("The word is not palidrome")
        break
    elif el == (leng_of_the_word//2)-1:
        print("The word is palidrome")