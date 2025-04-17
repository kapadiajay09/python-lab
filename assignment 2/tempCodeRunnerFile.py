test = int(input("enter the number of test cases\n"))

number=[]

for i in range(test):

    number.append(int(input("enter the number\n")))

for i in range(test):
        count = 0

        original_number=number[i]

        while number[i]!=0:


            rem = number[i]%10

            if original_number%rem==0:
                count += 1
            number[i]=number[i]//10
        print(count)


