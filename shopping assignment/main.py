from shopping import Shopping

def make_list():
    shopping_list=[]
    
    while True:
        num_of_items=eval(input("How many items are you going to buy? "))
        if num_of_items<1:
            print("You have to buy at leaaast one item")
        else:
            break
    
    for i in range(num_of_items):
        while True:
            item_name=input("Enter the name of the item: ")
            amt=eval(input("How many pounds? "))
            item=Shopping(item_name,amt)
            if item_name=="" or item.get_price()==0:
                print("You need to enter a valid name.")
            elif amt<0:
                print("Amount has to be more than 0")
            else:
                break
        shopping_list.append(item)
    
    return shopping_list

def display(list_of_items):
    print("-"*50)
    print("Here is the list of items that you purchased: ")
    for i in range(len(list_of_items)):
        print(f"Item {i+1}")
        print(list_of_items[i].__str__()+"\n")

def calculate_amount(list_of_items):
    total=0
    for i in range(len(list_of_items)):
        total+=list_of_items[i].total_price()
    return total

# shopping_list=make_list()
# display(shopping_list)
# print(f"Total amount: ${calculate_amount(shopping_list)}")

    