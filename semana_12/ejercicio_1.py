class BankAccount:
    balance = 0
    
    def deposit_money(self):
        account = int(input("Deposit money..."))
        self.balance = self.balance + account
         
    def withdraw_money(self):
        withdraw = int(input("I want to withdraw...$ "))
        self.balance = self.balance - withdraw
                     
class SavingAccounts(BankAccount):
    min_balance = 0
    
    def show_balance_result(self):
        
        self.withdraw_money()
        if self.balance >= self.min_balance:
            print(f"The account balance is: {self.balance}")   
        else:
            print(f"No tiene disponible...")
            
my_account = SavingAccounts()
my_account.deposit_money()
my_account.show_balance_result()         