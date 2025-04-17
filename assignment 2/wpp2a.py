word=input("enter the word\n")

list = list(word)

for i in range(len(list)):
    if i %2 == 0 :
        list[i] = list[i].lower()
    else:
        list[i] = list[i].upper()

str = ''.join(list)
print(str)
    