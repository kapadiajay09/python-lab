def generate_magic_square(n):
    if n % 2 == 1:
        magic_square = [[0] * n for _ in range(n)]
        i, j = 0, n // 2
        for num in range(1, n * n + 1):
            magic_square[i][j] = num
            new_i, new_j = (i - 1) % n, (j + 1) % n
            if magic_square[new_i][new_j]:
                i += 1
            else:
                i, j = new_i, new_j
    elif n % 4 == 0:
        magic_square = [[(i * n + j + 1) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if (i % 4 == j % 4) or (i % 4 + j % 4 == 3):
                    magic_square[i][j] = n * n - (i * n + j)
    else:
        raise NotImplementedError("Specialized methods required for singly even squares.")
    return magic_square

def print_magic_square(square):
    for row in square:
        print(" ".join(f"{val:3}" for val in row))

sizes = [4, 5, 6, 7, 8]
for size in sizes:
    try:
        print(f"\nMagic Square for N={size}:\n")
        magic_square = generate_magic_square(size)
        print_magic_square(magic_square)
    except NotImplementedError:
        print(f"Magic Square generation for N={size} is not implemented yet.")