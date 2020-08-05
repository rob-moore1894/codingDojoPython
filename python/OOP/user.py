class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    # make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
    def make_withdawal(self, amount):
        self.account_balance -= amount
        return self

    # display_user_balance(self) - have this method print the user's name and account balance to the terminal
    def display_user_balance(self):
        print(f"{self.name}, {self.account_balance}")
        return self
    
    # add a transfer_money method
    def transfer_money(self, transfer_to, amount):
        self.make_withdawal(amount)
        transfer_to.make_deposit(amount)
        self.display_user_balance()
        transfer_to.display_user_balance()
        return self

# Create 3 instances of the User class
user1 = User("Rob", "rob@email.com")
user2 = User("Diego", "diego@email.com")
user3 = User("Steven", "steven@email.com")

print(user1.name)
print(user2.name)
print(user3.name)

user1.make_deposit(100).make_deposit(200).make_deposit(100).make_withdawal(500).display_user_balance()

user2.make_deposit(100).make_deposit(250).make_withdawal(50).make_withdawal(100).display_user_balance()

user3.make_deposit(1000).make_withdawal(25).make_withdawal(18).make_withdawal(22).display_user_balance()

user3.transfer_money(user1,100)