student_names = []

for i in range(10):
    while True:
        name = input(f"Enter the name of student {i+1}: ")
        if len(name) <= 15:
            student_names.append(name)
            break
        else:
            print("Name is too long. Please enter a name with 15 or fewer characters.")

reversed_names = [name[::-1] for name in student_names]

print("\nReversed names of the students:")
for name in reversed_names:
    print(name)