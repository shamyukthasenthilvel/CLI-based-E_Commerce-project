import uuid
import cart
import product_management
import header

class Order:
    def __init__(self):
        self.total1 = cart.Cart()
        self.pro = product_management.ProductManagement()
        self.head = header.Header()  
    def checkout(self):
        print("{:<12}{:<10}".format("Product", "Count"))
        print("-" * 30)
        for dress, quan in self.total1.cart.items():
            print("{:<12}{:<10}".format(dress, quan))
        total = 0
        for dress, quan in self.total1.cart.items():
            for item in self.pro.product_list:
                if item[0].lower() == dress:
                    total += item[2] * quan
        self.total1.total = total
        print("Total        :", self.total1.total)
        self.head.checkout()  

    def payment(self):
        self.checkout()
        while True:
            inp = int(input("pay here: "))
            if inp == self.total1.total:
                print("paid")
                return True
            elif inp > self.total1.total:
                balance = inp - self.total1.total
                print("paid , here is your balance:", balance)
                return True
            elif inp < self.total1.total:
                balance = self.total1.total - inp
                while True:
                    inp1 = int(input(f"pay the balance amt {balance}: "))
                    if inp1 == balance:
                        print("paid")
                        return True
                    elif inp1 > balance:
                        print("paid and here is your balance:", inp1 - balance)
                        return True
                    else:
                        print("here is your cash , just try again to pay")
                        break
        self.head.product()  

    def invoice(self):
        if self.payment():
            unique_id = str(uuid.uuid4())
            f = open(f"C:/Users/DELL/Desktop/shamy/Projects/E_Commerce(python)/Invoices/Invoice_{unique_id}.txt", "w")
            f.write("Invoice\n")
            f.write(f"Invoice ID: {unique_id}\n\n")
            for dress, quan in self.total1.cart.items():
                f.write(f"{dress} - {quan}\n")
            f.write(f"Total: {self.total1.total}\n")
            f.close()
            print("Invoice saved ")
            self.head.user()  





            
                



