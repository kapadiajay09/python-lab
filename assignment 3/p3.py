test = int(input("Enter the number of test cases:"))  

cycles =[]

for i in range (test):
    cycles.append(int(input()))
for i in range(test):
    
    height_tree = 1  
    
    for j in range(cycles[i]):
        if j % 2 == 0:
            height_tree *= 2  
        else:
            height_tree += 1 
    
    print("The height of tree is ",height_tree)  
