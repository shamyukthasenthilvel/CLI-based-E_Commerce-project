class Header:
    def __init__(self, email, product_manager):
        self.email = email
        self.pm    = product_manager

    def run(self):
        while True:
            print(f"\nHello {self.email}! What would you like to do?")
            print("1. View all products")
            print("2. Search for a product")
            print("3. View cart")
            print("4. Add to cart")
            print("5. Remove from cart")
            print("6. Checkout")
            print("7. Generate Invoice")
            print("8. Logout")

            choice = input("Choose (1–8): ").strip()

            if choice == "1":
                self.pm.handle_list()
            elif choice == "2":
                self.pm.handle_search()
            elif choice == "3":
                self.pm.handle_cart()
            elif choice == "4":
                self.pm.handle_add_to_cart()
            elif choice == "5":
                self.pm.handle_remove_from_cart()
            elif choice == "6":
                self.pm.handle_checkout()
            elif choice == "7":
                self.pm.handle_invoice()
            elif choice == "8":
                print("Thank you for shopping with us!\n")
                break
            else:
                print("Invalid choice")

