#class Overload:
#    def __init__(self):
#      pass
#    def __init__(self,b):
#      pass
  
    
#me = Overload("Bob")
    
#me2 = Overload("Bob",20)
#print str(me)

def list_extend_many(lists):
    result = []
    i = 0
    while i < len(lists): 
        result += lists[i]
        print result
        i += 1
    return result
print list_extend_many([[1,2], [3], [4, 5, 6], [7]])

#6a question 8.
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.fees = 0
               
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance = self.balance + amount
        
        
       
    def withdraw(self, amount):
        """Withdraws the amount from the account.  Each withdrawal resulting in a negative balance also deducts a fee of 5 dollars from the balance."""
        self.balance = self.balance - amount
        if self.balance < 0:
           self.balance -=5
           self.fees += 5 
        
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance
    def get_fees(self):
        """Returns the total fees ever accrued in the account."""
        
        return self.fees
my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5) 
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50) 
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
print my_account.get_balance(), my_account.get_fees()