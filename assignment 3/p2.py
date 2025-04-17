test = int(input("Enter the number of test cases"))
cases = []
print("Enter the test cases")
for i in range (test):
    cases.append(int(input()))
print(cases)
for i in range (test):
    flag = 0
    if cases[i] == 0:
        print("IsFibo")
        flag =1
        continue
    elif cases[i] == 1:
        print("IsFibo")
        flag = 1
        continue
    a = 0
    b = 1
    c = a+b
    while c<= cases[i]:
        a = b
        b = c
        c = a+b
        if c == cases[i]:
            flag = 1
    if flag == 0:
        print("IsNotFibo")
    else:
        print("IsFibo")
        
    
    