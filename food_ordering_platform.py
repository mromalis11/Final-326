def display_menu():
    """Function to display the menu to the user."""
    menu = {
        1: ("Pizza", 10.00),
        2: ("Burger", 5.00),
        3: ("Pasta", 8.50),
        4: ("Salad", 6.75)
    }
    
    print("Here is our menu:")
    for key, (item, price) in menu.items():
        print(f"{key}: {item} - ${price}")
    
    return menu

def take_order(menu):
    """Function to take the user's order and generate an order number."""
    try:
        choice = int(input("Please enter the number of the item you'd like to order: "))
        if choice in menu:
            item, price = menu[choice]
            print(f"You've ordered {item} which costs ${price}.")
            return True
        else:
            print("Sorry, that's not a valid option.")
            return False
    except ValueError:
        print("Please enter a valid number.")
        return False

def main():
    """Main function to run the order process."""
    name = input("Please enter your name: ")
    print(f"Welcome, {name}!")
    
    menu = display_menu()
    order_success = take_order(menu)
    
    if order_success:
        # Simple way to generate an order number
        # In a real application, you'd have a more complex system for this
        from random import randint
        order_number = randint(100, 999)
        print(f"Thank you for your order, {name}. Your order number is {order_number}.")

if __name__ == "__main__":
    main()
