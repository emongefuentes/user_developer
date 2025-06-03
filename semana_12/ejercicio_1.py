class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def deposit_money(self):
        account = int(input("Deposit money..."))
        self.balance = self.balance + account
         
    def withdraw_money(self,result):
        if self.balance - result < self.min_balance:
        
            print("you don't have that amount of money...")
        else:
            self.balance = self.balance - result
            print(f"Your final balance is: ${self.balance}")
                     
class SavingAccounts(BankAccount):
    min_balance = 0
    
    def show_balance_result(self):
        result = int(input("I want to withdraw... "))
        self.withdraw_money(result)
            
my_account = SavingAccounts()
my_account.deposit_money()
my_account.show_balance_result()         