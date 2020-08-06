class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    #deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount
        return self

    # withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    # display_account_info(self) - print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    # yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.balance > 0:
            addInt = self.balance * self.int_rate
            self.balance += addInt
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def make_deposit(self, amount):
        self.account.deposit += amount
        return self

    # make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
    def make_withdawal(self, amount):
        self.account.withdraw -= amount
        return self

    # display_user_balance(self) - have this method print the user's name and account balance to the terminal
    def display_user_balance(self):
        print(f"{self.name}, {self.account.balance}")
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