import math

def count_squares(A, B):
    start = math.ceil(math.sqrt(A))
    end = math.floor(math.sqrt(B))
    return max(0, end - start + 1)


Test = int(input("Enter number of test cases: "))
for _ in range(Test):
    A, B = map(int, input().split())
    print(count_squares(A, B))
