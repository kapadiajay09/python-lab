def min_swaps(arr):
    n = len(arr)
    arrpos = [*enumerate(arr)]
    arrpos.sort(key=lambda it: it[1])
    vis = {k: False for k in range(n)}
    ans = 0

    for i in range(n):
        if vis[i] or arrpos[i][0] == i:
            continue

        cycle_size = 0
        x = i
        while not vis[x]:
            vis[x] = True
            x = arrpos[x][0]
            cycle_size += 1

        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans

# Example usage:
heights = [5, 1, 3, 2, 4]
print("Minimum swaps required:", min_swaps(heights))