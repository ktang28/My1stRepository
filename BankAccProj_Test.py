class BankAccount:
    nextAccountNum = 123456

    def __init__(self, acc_name, account_num,balance=0):
        self.acc_name = acc_name
        self.account_num = BankAccount.nextAccountNum
        self.account_type = self.get_account_type()
        self.balance = balance
        self.transaction_history = []
        BankAccount.nextAccountNum = BankAccount.nextAccountNum + 1
        print("The account is created")

    def get_account_type(self):
        while True:
            account_type = input("Enter account type (Savings/Checking): ").strip().capitalize()
            if account_type in ["Savings", "Checking"]:
                return account_type
            else:
                print("Invalid account type. Please enter 'Savings' or 'Checking'.")


    def deposit_money(self):
        amount = float(input(' Please enter amount to be deposited:'))
        if amount > 0:
            self.balance = self.balance + amount
            self.transaction_history.append(f"Deposited: ${amount}")
            print('\n Amount deposited:', amount)
            return self.balance
        else:
            print('Invalid Deposit Amount')
            return None

    def withdraw_money(self):
        amount = float(input(' Please enter amount to be withdrawn:'))
        if self.balance >= amount:
            self.balance = self.balance - amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            print('\n Amount withdrawn:', amount)
        else:
            print('\n Insufficient balance')

    def display_account_info(self):
        print(f"Name: {self.acc_name}")
        print(f"Account number: {self.account_num}")
        print(f"Account type: {self.account_type}")

    def check_balance(self):
        self.balance = self.balance

        print(f"Updated balance for {self.acc_name}: {self.balance}")

    def get_transaction_history(self):
        print(f"Transaction history for {self.account_type} account {self.account_num}:")
        for transaction in self.transaction_history:
            print(transaction)
        return self.transaction_history

def main():

    while True:
        print("\n Welcome! Please entry your selection:")
        print("1: Create a new account    2: Deposit money   3: Withdraw money  4: Display account name, number & type  5: Update account balance 6: Transaction history  0:Exit")

        choice = input("Choose an option (1/2/3/4/5/6/0): ")

        if choice == '1':

            name = input("Enter your name: ")
            account_num = BankAccount.nextAccountNum + 1

            account = BankAccount(name,account_num,balance =0,)

        elif choice == '2':
            account.deposit_money()

        elif choice == '3':
            account.withdraw_money()
        elif choice == '4':
            account.display_account_info()

        elif choice == '5':
            account.check_balance()

        elif choice == '6':
            account.get_transaction_history()

        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
