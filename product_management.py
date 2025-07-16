import uuid
class ProductManagement:
    def __init__(self):
        self.product_list = [
            ["T‑shirt",  5,  345],
            ["Skirt",   10,  450],
            ["Tunics",  10,  500],
            ["Pants",   45,  600],
            ["Kurti",    7,  785],
            ["Jeans",   60, 1000],
            ["Gown",    45,  550],
            ["Palazzo", 45,  660]
        ]
        self.cart = []          
    def list_products(self):
        print("\n{:<3}{:<12}{:<10}{:<10}".format("#", "Product", "Qty", "Price"))
        for idx, (pro, q, p) in enumerate(self.product_list, 1):
            print("{:<3}{:<12}{:<10}{:<10}".format(idx, pro, q, p))

    def search(self, term):
        for pro, q, p in self.product_list:
            if pro.lower() == term.lower():
                return pro, q, p
        return None

    def handle_list(self):
        self.list_products()

    def handle_search(self):
        name = input("Enter product name: ").strip()
        found = self.search(name)
        if found:
            pro, q, p = found
            print(f" {pro} available – Qty: {q}, Price: {p}")
            add = input("Add to cart? (y/n): ").lower()
            if add == 'y':
                self.cart.append((pro, 1, p))
                print("Added to cart")
        else:
            print(" Item not found")

    def handle_cart(self):
        if not self.cart:
            print(" Cart empty")
            return
        print("\nYour Cart:")
        total = 0
        for idx, (pro, qty, price) in enumerate(self.cart, 1):
            line_total = qty * price
            total += line_total
            print(f"{idx}. {pro:<10} x{qty}  ₹{line_total}")
        print(f"Total: ₹{total}")
    

    def handle_add_to_cart(self):
        self.list_products()
        name = input("Enter product name to add: ").strip()
        quantity = int(input("Enter quantity: "))
        for i, (pro, stock, price) in enumerate(self.product_list):
            if pro.lower() == name.lower():
                if quantity <= stock:
                    self.cart.append((pro, quantity, price))
                    self.product_list[i][1] -= quantity  
                    print("Added to cart")
                else:
                    print("Not enough stock available")
                return
        print("Product not found")

    def handle_remove_from_cart(self):
        if not self.cart:
            print("Cart is empty")
            return
        name = input("Enter product name to remove: ").strip()
        for i, (pro, qty, price) in enumerate(self.cart):
            if pro.lower() == name.lower():
                self.cart.pop(i)
                print("Removed from cart")
                return
        print("Item not in cart")
    

    def handle_checkout(self):
        if not self.cart:
            print("Cart is empty, cannot checkout.")
            return

        print("{:<12}{:<10}{:<10}".format("Product", "Qty", "Subtotal"))
        print("-" * 35)
        total = 0
        for pro, qty, price in self.cart:
            subtotal = qty * price
            print("{:<12}{:<10}{:<10}".format(pro, qty, subtotal))
            total += subtotal
        print(f"Total: ₹{total}")
        self.total_amount = total

    def handle_payment(self):
        if not hasattr(self, 'total_amount'):
            print("Please checkout first.")
            return

        while True:
            inp = int(input("Pay here: ₹"))
            if inp == self.total_amount:
                print("Paid successfully.")
                return True
            elif inp > self.total_amount:
                print(f"Paid. Balance returned: ₹{inp - self.total_amount}")
                return True
            elif inp < self.total_amount:
                diff = self.total_amount - inp
                while True:
                    inp2 = int(input(f"Please pay remaining ₹{diff}: "))
                    if inp2 == diff:
                        print("Paid completely.")
                        return True
                    elif inp2 > diff:
                        print(f"Paid. Balance returned: ₹{inp2 - diff}")
                        return True
                    else:
                        print("Still less. Try again.")
                        break
        return False

    def handle_invoice(self):
        if self.handle_payment():
            uid = str(uuid.uuid4())
            file_path = f"C:/Users/DELL/Desktop/shamy/Projects/E_Commerce(python)/New folder/Invoice/Invoice_{uid}.txt"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("Invoice\n")
                f.write(f"Invoice ID: {uid}\n\n")
                for pro, qty, price in self.cart:
                    f.write(f"{pro} x {qty} = ₹{qty * price}\n")
                f.write(f"\nTotal: ₹{self.total_amount}")

            self.cart.clear()  
