class Bank_account:
    interest_rate = 0.03
    balance = 0
    all_accounts = []
    
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
        Bank_account.all_accounts.append(self)

    def deposit(self, amount):
        #increases the account balance by the given amount
        self.balance += amount
        print('===========')
        print(f'Your new balance is: ${self.balance}.')
        return self
        
    def withdraw(self, amount):
        # decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
            print(f'Your balance is: {self.balance}')
        return self
    
    def display_account_info(self):
        #print to the console: eg. "Balance: $100"
        print('===========')
        print(f'Your available balance to use is: ${self.balance}')
        return self

    def yield_interest(self):
        #increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        return self
    @classmethod
    def print_bank_accounts(cls):
        # print all instances of a Bank Account's info
        for account in cls.all_accounts:
            # print(f'You have {len(cls.all_accounts)}: {cls.all_accounts[account]}')
            account.display_account_info()


    
# Create 2 accounts
checking_account = Bank_account(0.03, 0)
# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
print('Checking Account:')
checking_account.deposit(200).deposit(150).deposit(180).withdraw(700).yield_interest()
print('---------')

saving_account = Bank_account(0.05, 200)
# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
print('Saving Account:')
saving_account.deposit(300).deposit(470).withdraw(220).withdraw(100).withdraw(290).withdraw(100).yield_interest()
print('---------')
Bank_account.print_bank_accounts()

    
