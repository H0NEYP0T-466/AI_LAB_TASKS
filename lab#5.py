shopping_list=['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

def addShoppingItem(name):
    shopping_list.append(name)
    return shopping_list

def removeShoppingItem(name):
    shopping_list.remove(name)
    return shopping_list

def displayShoppingList():
    for item in shopping_list:
        print(item)

def loopfunction():
    while True:
        print("\nShopping List Menu:")
        print("1. View Shopping List")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            displayShoppingList()
        elif choice == '2':
            item_to_add = input("Enter the item to add: ")
            addShoppingItem(item_to_add)
            print(f"{item_to_add} has been added to the shopping list.")
        elif choice == '3':
            item_to_remove = input("Enter the item to remove: ")
            if item_to_remove in shopping_list:
                removeShoppingItem(item_to_remove)
                print(f"{item_to_remove} has been removed from the shopping list.")
            else:
                print(f"{item_to_remove} is not in the shopping list.")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


loopfunction()
