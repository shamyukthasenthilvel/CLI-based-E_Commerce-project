import re

class UserManagement:
    def __init__(self):
        self.user = {"shamy@gmail.com": "shamy@12345"}

    def login_or_register(self):
        print("\nWelcome to Amazon Great Indian Festival!")
        while True:
            action = input("Registration (r) / Login (l): ").lower()

            if action not in ("l", "r"):
                print("Please enter only 'l' or 'r'")
                continue

            email = input("enter email: ")
            if not re.match(r'^[a-zA-Z0-9]+@gmail\.com$', email):
                print("Invalid email format (must be @gmail.com)")
                continue

            password = input("enter password (≥ 8 characters): ")
            if len(password) < 8:
                print("Password is weak")
                continue

            if action == "l":
                if self.user.get(email) == password:
                    print("Successfully logged in")
                    return email
                print("Invalid credentials")
                return None
            else:   
                if email in self.user:
                    print("Account already exists, choose login instead")
                    return None
                self.user[email] = password
                print("Successfully registered")
                return email
