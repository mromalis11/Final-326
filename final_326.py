from random import randint

class Order:
    """Class to be the order where there will be a unique order number and total price after order"""
    def __init__(self, order_number):
        self.order_number = order_number
        self.items = []
        self.total_price = 0.0

    def add_item(self, item_name, price):
        self.items.append((item_name, price))
        self.total_price += price

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.total_price -= item[1]
                self.items.remove(item)
                break

    def calculate_total_price(self):
        return self.total_price

def display_menu():
    """Function to display the menu to the user where they are numbered 1-4."""
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
    """Function to take the user's order, generate an order number, can keep ordering until input '0' to end"""
    order_number = randint(100, 999)
    order = Order(order_number)
    
    while True:
        try:
            choice = int(input("Please enter the number of the item you'd like to order (0 to finish): "))
            if choice == 0:
                break
            elif choice in menu:
                item, price = menu[choice]
                print(f"You've added {item} which costs ${price}.")
                order.add_item(item, price)
            else:
                print("Sorry, that's not a valid option.")
        except ValueError:
            print("Please enter a valid number.")
    
    if not order.items:
        print("You didn't order anything.")
        return False, order
    
    print("Here is your order:")
    for idx, (item, price) in enumerate(order.items, start=1):
        print(f"{idx}: {item} - ${price}")
    
    print(f"Total price: ${order.calculate_total_price()}")
    
    return True, order

def get_feedback() -> int:
    """This function is for the feedback part where the user will be prompted to rate the system 1-10 scale."""
    while True:
        try:
            feedback = int(input("Please rate your experience with us on a scale of 1-10 (10 being the best): "))
            if 1 <= feedback <= 10:
                return feedback
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main function to run the order process. User will enter their name and then proceed to order and receive their order number."""
    name = input("Please enter your name: ")
    print(f"Welcome, {name}!")
    
    menu = display_menu()
    order_success, order = take_order(menu)
    
    if order_success:
        print(f"Thank you for your order, {name}. Your order number is {order.order_number}.")
        
        feedback = get_feedback()
        print("Thank you for your feedback!")

"""Run the code in the terminal like so: 'python final_326.py' and then the code will run asking for your name, then asking what you want from the menu, then after you order it will provide an order number and ask for your feedback"""
if __name__ == "__main__":
    main()
