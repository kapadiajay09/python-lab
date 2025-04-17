dict= {}

while True:
    name = input("enter the name of product or 'done' to finish:\n")
     
    if name.lower()== 'done':

        break

    price= input("enter the price :\n")

    dict[name]=float(price)

while True:
    query=input("enter the query  or 'quit' to exit\n")
    
    if query in dict:
        print("price=",dict[query])

    if query.lower()=='quit':
        break
    if(not(query in dict)):
        print("the price of entered query is not found\n")


       
    


