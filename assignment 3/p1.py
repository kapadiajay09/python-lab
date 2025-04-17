num = int(input("Enter number"))
sum = 0
while num//10 !=0:
    while num!=0:
        r = num%10
        sum = sum + r
        num = num//10
    num = sum
    sum = 0
print("The digital root is",num)
