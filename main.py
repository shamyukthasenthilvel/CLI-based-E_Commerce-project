from user_management import UserManagement
from product_management import ProductManagement
from header import Header
from admin import admin1


print("=== Python E‑Commerce Store ===")
um = UserManagement()

try:
    while True:
        email = um.login_or_register()
        if email:
            if email == "shamy@gmail.com":
                admin1(email) 
                continue      
            else:
                pm  = ProductManagement()
                hdr = Header(email, pm)
                hdr.run()
        else:
            print("Login/Registration failed. Try again.")
except Exception as e:
    print(f"Something went wrong: {e}")


