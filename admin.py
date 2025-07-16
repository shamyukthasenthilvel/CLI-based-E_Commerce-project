import os

def admin1(email):
    print(f"\nAdmin Mode: Viewing All Orders for {email}")
    path = r"C:\Users\DELL\Desktop\shamy\Projects\E_Commerce(python)\New folder\Invoice"
    if not os.path.exists(path):
        print("No invoices found.")
    else:
        for file in os.listdir(path):
            if file.startswith("Invoice_") and file.endswith(".txt"):
                with open(os.path.join(path, file), "r") as f:
                    print(f.read())
                    print("-" * 40)

    while True:
        choice = input("Enter '4' to logout: ").strip()
        if choice == "4":
            print("Logged out from Admin.")
            break
        else:
            print("Invalid. Only '4' is allowed.")



        

