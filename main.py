class Customer:
    
    def __init__(self, name, balance, savings):
        self.name = name 
        self.balance = balance
        self.savings = savings
     
# Methods involve: Transfer, deposit, withdraw, save.                 
    def transfer(self, amount):
        self.balance = self.balance - amount
        return self.balance
        
    def withdraw(self, amount):
        self. balance = self. balance - amount 
        return [amount, self.balance]
        
    def deposit (self, amount ):
        self.balance = self.balance + amount
        return [amount, self.balance]
    
    def transactions (self):
        pass

print("1. Deposit money")
print("2. Withdraw money")
print ("3. Send money")
print ("4. Check Transactions")


while True: 
    x = int(input("Select a number from 1 - 4: "))
    if int(x) not in range (1,5):
        continue
        
    if x == 1:
       dep = input("Type in deposit amount: ")
       bal = deposit(dep)
       print(f"Deposit successful. your balance is {bal}")
       break 
    if x == 2:
        draw = input("Type withdrawal amount" )
        bal = withdraw(draw)
        print(f"Withdraw successful, your balance is {bal}")
        break
    if x == 3:
        ben= input("Type in Beneficiary name") 
        ben_acc = input("Beneficiary account ")
        tf_amount = input("Amount to send:")

        bal = transfer(tf_amount)
        print(f"Transfer of {tf_amount} to {ben_acc} was successful. Your balance is {bal}")
        break
    if x == 4:
        pass



