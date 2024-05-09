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
    """Function to take the user's order and generate an order number. Users can keep ordering items until they input '0' to finish order"""
    order = []
    while True:
        try:
            choice = int(input("Please enter the number of the item you'd like to order (0 to finish): "))
            if choice == 0:
                break
            elif choice in menu:
                item, price = menu[choice]
                print(f"You've added {item} which costs ${price}.")
                order.append((item, price))
            else:
                print("Sorry, that's not a valid option.")
        except ValueError:
            print("Please enter a valid number.")
    
    if not order:
        print("You didn't order anything.")
        return False, []
    
    print("Here is your order:")
    total_price = 0
    for idx, (item, price) in enumerate(order, start=1):
        print(f"{idx}: {item} - ${price}")
        total_price += price
    
    print(f"Total price: ${total_price}")
    
    return True, order

def main():
    """Main function to run the order process. User will enter their name and then proceed to order and receive their order number."""
    name = input("Please enter your name: ")
    print(f"Welcome, {name}!")
    
    menu = display_menu()
    order_success, order = take_order(menu)
    
    if order_success:
        from random import randint
        order_number = randint(100, 999)
        print(f"Thank you for your order, {name}. Your order number is {order_number}.")
        
        while True:
            try:
                feedback = int(input("Please rate your experience with us on a scale of 1-10 (10 being the best): "))
                if 1 <= feedback <= 10:
                    print("Thank you for your feedback!")
                    break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Please enter a valid number.")

if __name__ == "__main__":
    main()
