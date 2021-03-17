import pandas as pd

def shopping_list():
    grocery_list = {}    #(product:[quantity,price])
    
    budget = int(input("Enter your Budget : "))
    
    while True:
        print("1.Add an item\n")
        print("2.Exit\n")
        opt = int(input("Enter your choice : "))
        if opt == 2:
            for key,value in grocery_list.items():
                if value[1] < budget:
                    print(f"With the amount left you can buy {key}\n")
                    break
            break
        elif opt == 1:
            prod = str(input("Enter product : "))
            print("\r")
            quant = str(input("Enter quantity : "))
            print('\r')
            price = int(input("Enter price : "))
            print('\r')
            
            if price > budget:
                print(f"Can't buy {prod} as your budget is {budget} which is less than the cost of {prod}\n")
                continue
                
            if prod not in grocery_list:
                grocery_list[prod] = [quant,price]
            else:
                budget += grocery_list[prod][1]
                grocery_list[prod][1] = price
                grocery_list[prod][0] = quant
                
            budget -= price
            print(f"Amount left : {budget}")
        else:
            print("Not a valid option ,try again\n")
            continue
    print(f"Grocery list is : \n {pd.DataFrame.from_dict(grocery_list,orient='index',columns=['Quantity','Price'])}")        
            
if __name__ == "__main__":
    shopping_list()

