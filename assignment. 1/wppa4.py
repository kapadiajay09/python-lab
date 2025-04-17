
equiv_classes = {i: set() for i in range(5)}

for num in range(1, 10001):
    remainder = num % 5
    equiv_classes[remainder].add(num)
    
union_of_classes = set()
for cls in equiv_classes.values():
    union_of_classes.update(cls)

original_set = set(range(1, 10001))

if original_set == union_of_classes:
    print("its valid");
else:
    print("it's invalid");