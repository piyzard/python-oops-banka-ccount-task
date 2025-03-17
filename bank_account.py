class BankAccount:
    total_accounts = 0  
    all_accounts = []  
    
    def __init__(self, account_holder, initial_balance=0, account_type='Savings'):
        if not account_holder:
            raise ValueError("Account holder name cannot be empty.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_type = account_type
        self.transactions = []
        
        BankAccount.total_accounts += 1
        BankAccount.all_accounts.append(self)
        print(f"Account created for {self.account_holder} ({self.account_type} Account).")
    
    def deposit(self, amount):
        if not self.validate_amount(amount):
            raise ValueError("Invalid deposit amount.")
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")
        print(f"₹{amount} deposited. New balance: ₹{self.balance}")
    
    def withdraw(self, amount):
        if not self.validate_amount(amount) or amount + 10 > self.balance:
            raise ValueError("Invalid withdrawal amount or insufficient funds.")
        self.balance -= (amount + 10)  # ₹10 transaction fee
        self.transactions.append(f"Withdrew ₹{amount} (Fee ₹10)")
        print(f"₹{amount} withdrawn (Fee ₹10). New balance: ₹{self.balance}")
    
    def transfer(self, recipient, amount):
        if not isinstance(recipient, BankAccount):
            raise ValueError("Recipient must be a BankAccount instance.")
        if not self.validate_amount(amount) or amount > self.balance:
            raise ValueError("Invalid transfer amount or insufficient funds.")
        
        self.balance -= amount
        recipient.balance += amount
        self.transactions.append(f"Transferred ₹{amount} to {recipient.account_holder}")
        recipient.transactions.append(f"Received ₹{amount} from {self.account_holder}")
        print(f"Transferred ₹{amount} to {recipient.account_holder}. New balance: ₹{self.balance}")
    
    def check_balance(self):
        print(f"Current balance for {self.account_holder}: ₹{self.balance}")
    
    def get_transaction_history(self):
        print(f"Transaction history for {self.account_holder}:")
        for transaction in self.transactions:
            print(transaction)
    
    @classmethod
    def total_bank_accounts(cls):
        return f"Total bank accounts: {cls.total_accounts}"
    
    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int, float)) and 0 < amount <= 50000

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance=0):
        super().__init__(account_holder, initial_balance, account_type='Savings')
        if initial_balance < 1000:
            raise ValueError("Savings Account requires a minimum balance of ₹1000.")
    
    def apply_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        self.transactions.append(f"Interest of ₹{interest} applied.")
        print(f"₹{interest} interest applied. New balance: ₹{self.balance}")

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, initial_balance=0):
        super().__init__(account_holder, initial_balance, account_type='Current')

def main():
    accounts = {}
    while True:
        print("\nBank Account Management System")
        print("1. Open Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Check Balance")
        print("6. Transaction History")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter account holder name: ")
            acc_type = input("Enter account type (Savings/Current): ").capitalize()
            initial_balance = float(input("Enter initial balance: "))
            if acc_type == 'Savings':
                accounts[name] = SavingsAccount(name, initial_balance)
            else:
                accounts[name] = CurrentAccount(name, initial_balance)

        elif choice == '2':
            name = input("Enter account holder name: ")
            if name in accounts:
                amount = float(input("Enter deposit amount: "))
                accounts[name].deposit(amount)
            else:
                print("Account not found.")

        elif choice == '3':
            name = input("Enter account holder name: ")
            if name in accounts:
                amount = float(input("Enter withdrawal amount: "))
                accounts[name].withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            sender = input("Enter your name: ")
            recipient = input("Enter recipient's name: ")
            if sender in accounts and recipient in accounts:
                amount = float(input("Enter transfer amount: "))
                accounts[sender].transfer(accounts[recipient], amount)
            else:
                print("One or both accounts not found.")

        elif choice == '5':
            name = input("Enter account holder name: ")
            if name in accounts:
                accounts[name].check_balance()
            else:
                print("Account not found.")

        elif choice == '6':
            name = input("Enter account holder name: ")
            if name in accounts:
                accounts[name].get_transaction_history()
            else:
                print("Account not found.")

        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
