def max_xor(L,R):
    max_value = 0
    for A in range(L,R+1):
        for B in range (A,R+1):
            max_value = max(max_value,A^B)
    return max_value

L,R=map(int , input().split())

print(max_xor(L,R))