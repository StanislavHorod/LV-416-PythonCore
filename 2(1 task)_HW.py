text = ("Simple is better than complex.\n"+
"Complex is better than complicated.\n" +
"Flat is better than nested. \n" +
"Sparse is better than dense.\n"+
"Readability counts.\n"+
"Special cases aren't special enough to break the rules.\n"+
"Although practicality beats purity.\n"+
"Errors should never pass silently.\n"+
"Unless explicitly silenced.\n"+
"In the face of ambiguity, refuse the temptation to guess.\n"+
"There should be one-- and preferably only one --obvious way to do it.\n"+
"Although that way may not be obvious at first unless you're Dutch.\n"+
"Now is better than never.\n"+
"Although never is often better than *right* now.\n"+
"If the implementation is hard to explain, it's a bad idea.\n"+
"If the implementation is easy to explain, it may be a good idea.\n"+
"Namespaces are one honking great idea -- let's do more of those!\n")
words = text.split()
better = 0
newer = 0
iss = 0
for word in words:
    if word == "better":
        better += 1
    elif word == "newer":
        newer += 1
    elif word == "is":
        iss += 1

for word in range(len(text)):
    repla = text.replace("i", "&")

print("The count of 'better' is: " + str(better) + 
    ";\nThe count of 'newer' is: " + str(newer) +
    ";\nThe count of 'is' is: " + str(iss))
print("\n\nEpic variant of the Python philosophy:\n\n"+text.upper())
print("\n\n Variant with replace 'i' to '&':\n\n"+repla)

