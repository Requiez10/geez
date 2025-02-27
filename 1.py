class BurgerKaSaken:
    def __init__(self):
        self.menu_prices = {
            "burger": 40,
            "fries": 30,
            "water": 20
        }
        self.items = []
        self.prices = []
        self.total = 0

    def display_menu(self):
        print("     𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐁𝐔𝐑𝐆𝐄𝐑 𝐊𝐀 𝐒𝐀𝐊𝐄𝐍!     \n")
        print("Menu: Burger, Fries, Water")
        print("        40     30     20 \n")

    def add_item_to_cart(self, item, quantity):
        if item in self.menu_prices and quantity > 0:
            for _ in range(quantity):
                price = self.menu_prices[item]
                self.items.append(item)
                self.prices.append(price)
            print(f"{quantity} {item.capitalize()}(s) added to your cart.")
        else:
            print("Invalid item or quantity.")

    def show_cart(self):
        print("\n     YOUR ITEMS     ")
        if self.items:
            for i in range(len(self.items)):
                print(f"{i + 1}. {self.items[i].capitalize()}: ₱{self.prices[i]:.2f}")
            print("----------------------")
            print(f"Your total is: ₱{self.total:.2f}")
        else:
            print("Your cart is empty!")

    def remove_item_from_cart(self, item_index):
        if 0 <= item_index < len(self.items):
            removed_item = self.items.pop(item_index)
            removed_price = self.prices.pop(item_index)
            print(f"{removed_item.capitalize()} has been removed from your cart.")
            self.total = sum(self.prices)
        else:
            print("Invalid item index.")

    def calculate_total(self):
        self.total = sum(self.prices)

    def checkout(self):
        print(f"\nYOUR TOTAL IS: ₱{self.total:.2f}")
        print("\n     THANK YOU FOR COMING!     ")

    def run(self):
        self.display_menu()

        while True:
            item = input("Enter an item to buy or q to quit: ").lower()
            
            if item == "q":
                break
            elif item in self.menu_prices:
                quantity = int(input(f"How many {item}s would you like to add? "))
                if quantity > 0:
                    self.add_item_to_cart(item, quantity)
                else:
                    print("Please enter a valid quantity greater than 0.")
            else:
                print("Invalid item. Please choose from the menu: Burger, Fries, Water.")

        self.calculate_total()
        
        while True:
            self.show_cart()
            
            if self.items:
                delete = input("\nDo you want to remove an item from your cart? (y/n): ").lower()
                if delete == 'y':
                    try:
                        item_to_remove = int(input("Enter the number of the item to remove (1-based index): ")) - 1
                        self.remove_item_from_cart(item_to_remove)
                        if not self.items:
                            print("Your cart is now empty.")
                            break
                    except ValueError:
                        print("Please enter a valid number.")
                elif delete == 'n':
                    break
                else:
                    print("Invalid input. Please try again.")
            else:
                break

        self.checkout()



burger_ka_saken = BurgerKaSaken()
burger_ka_saken.run()
