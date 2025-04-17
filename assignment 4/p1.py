def operations(str):
    operations = 0
    n = len(str)
    for i in range(n // 2):
        operations += abs(ord(str[i]) - ord(str[n - i - 1]))
    return operations

Test = int(input("Enter number of test cases: "))
for _ in range(Test):
    str = input("Enter the string: ")
    print(operations(str))
