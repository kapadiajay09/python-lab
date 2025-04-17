# r index
print("Rindex")
substring = 'cd'
str = 'abcdabcdabcd'
print("from right")
for i in range(len(str) - len(substring) , 0 ,-1):
    if str[i:i+len(substring)] == substring:
        print(i)
        break

print("\n \nRsplit")
def custom_rsplit(s, sep=None, maxsplit=-1):
    if sep is None:
        sep = ' '
    parts = s[::-1].split(sep[::-1], maxsplit)
    return [part[::-1] for part in parts][::-1]

s = "apple,banana,grape,orange"
result = custom_rsplit(s, ',', 2)
print(result)


print("\n \nRfind")
def custom_rfind(s, sub):
    return len(s) - s[::-1].find(sub[::-1]) - len(sub)

s = "hello world, welcome to the world"
sub = "world"
result = custom_rfind(s, sub)
print(result)


print("\n \nreplace")
def custom_replace(s, old, new):
    result = ''
    i = 0
    while i < len(s):
        if s[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
    return result

s = "hello world, welcome to the world"
old = "world"
new = "universe"
result = custom_replace(s, old, new)
print(result)

