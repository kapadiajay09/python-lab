def max_cut(K):
    a=(K+1)//2
    b=K//2
    return a*b

test=int(input())
for _ in range(test):
    K=int(input())
    print(max_cut(K))