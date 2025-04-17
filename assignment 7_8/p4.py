class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __eq__(self, other):
        return self.salary == other.salary


name1 = input("Enter first employee's name: ")
salary1 = float(input("Enter first employee's salary: "))
name2 = input("Enter second employee's name: ")
salary2 = float(input("Enter second employee's salary: "))

emp1 = Employee(name1, salary1)
emp2 = Employee(name2, salary2)

print(f"Total salary: {emp1 + emp2}")
print(f"Salary difference: {emp1 - emp2}")
if emp1 > emp2:
    print(f"{emp1.name} has a higher salary.")
elif emp1 < emp2:
    print(f"{emp2.name} has a higher salary.")
else:
    print("Both employees have the same salary.")
