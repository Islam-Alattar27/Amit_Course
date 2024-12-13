class Bank:
    def __init__(self):
        self.users = {} 
        
    def register(self, username, password):

        if username in self.users:
            print(f"Username {username} already exists. Please choose a different username")

        else:
            self.users[username] = { 'password': password, 'balance': 0 }
            print(f"User {username} registered successfully.")

    def login(self, username, password):

        if username in self.users and self.users[username]['password'] == password:
            print(f"User {username} logged in successfully.")  

        else:
            print("Invalid username or password.")

    def check_balance(self, username):
        
        if username in self.users:           
            balance = self.users[username]['balance']
            print(f"Current balance for {username}: ${balance}")
            
        else:
            print("User not found.")

    def deposit(self, username, amount):

        if amount > 0:
            self.users[username]['balance'] += amount
            print(f"${amount} deposited successfully. New balance: ${self.users[username]['balance']}")
            
        else:
            print("Deposit amount must be positive")

    def withdraw(self, username, amount):
        
        if amount <= 0:
            print("Amount must be positive")

        elif self.users[username]['balance'] >= amount:
            self.users[username]['balance'] -= amount
            print(f"${amount} withdrawn successfully. New balance: ${self.users[username]['balance']}")
            
        else:
            print(f"The Amount bigger than the balance -> {self.users[username]['balance']}")
            
    def info(self):
        print(f"Total users: {self.users}")
