'''
Created on Apr 14, 2019
Creates a checking account
@author: Rosalind Ng
'''
from Currencies import Currencies

class Account:
    '''
    Checking account
    '''
    def __init__(self, accNo, initBalance, owner):
        #initializes accNumber, initial balanace, and owner in the class
        try:
            #balance
            if(initBalance > 0):
                self.__balance = initBalance
            else:
                self.__balance = 0
            
            self.__accNo = str(accNo)
            self.__owner = str(owner)
            
        except TypeError:
            raise TypeError("balance is not a number")
        
    def getActNo(self):
        #returns acount number
        return self.__accNo
    
    def getBalance(self):
        #returns balance
        return self.__balance
    
    def printBalance(self):
        #return account number and balance as string :
        #Account Number: <value> Balance: $<value> CAD 
            return 'Account Number: {} Balance: ${:,.2f} CAD'.format(self.__accNo, self.__balance)
    
    def deposit(self, amount):
        #add amount to balance
        #returns true if successful, false otherwise
        
        #converts amount to CAD
        self.amt = self.__amtInCad(amount)
        
        #if amt > 0, add to balance
        if self.amt > 0:
            self.__balance += self.amt
            return True

        return False
    
    @staticmethod
    def __getExgRate(cur):
        #returns exchange rate of the currency to convert to CAD
        #1 CAD = 1 CAD
        #1 CAD = .5 USD
        #1 CAD = 10 MXN
        return Currencies.getValue(cur)
    

    def __amtInCad(self, amount):
        #converts amount to Canadian
        #example 100 USD = 200 CAD
        
        #splits amounts to num and cur
        num, cur = amount.split(" ")
        
        #get exchange rate
        eRate = self.__getExgRate(cur)
        
        return float(num) * eRate
    
    def withdraw(self, amount):
        #withdraws amount from account if balance > amount (CAD)
        #returns true if successful, false otherwise
        
        #if balance > amount(CAD) and amount > 0
        if self.__enoughCash(amount) and self.__positive(amount):
            self.__balance -= self.__amtInCad(amount)
            return True
        
        return False
    

    def __enoughCash(self, amount):
        #returns True if balance >= amount
        return self.__balance >=  self.__amtInCad(amount)
    
    
    def __positive(self, amount):
        #returns if amount is a positive value
        
        #get numeric value of amount
        num = amount.split(" ")[0]
        return float(num) > 0

    def getOwner(self):
        #return owner
        return self.__owner
        
    def isOwner(self, user):
        # check if user is owner
        return str(user) == self.__owner

class Checking(Account):
    '''
    Join class that inherits from Account, allows for more than one owner
    '''
    def __init__(self,accNo, initBalance, owner):
        super().__init__(accNo, initBalance, owner)
        
class Joint(Account):
    '''
    Join class that inherits from Account, allows for more than one owner
    '''
    def __init__(self, accNo, initBalance, owner):
        super().__init__(accNo, initBalance, owner)
        self.__owners = {str(owner)}
    
    def getOwners(self):
        #return owners
        return self.__owners
    
    def add_owner(self, owner):
        #add new owner if not already an owner
        if str(owner) not in self.__owners:
            self.__owners.add(str(owner))

            
    def remove_owner(self, owner):
        #remove owner if in set of owners
        if str(owner) in self.__owners:
            self.__owners.remove(str(owner))
    
    def isOwner(self, user):
        #check if user is owner
        if str(user) in self.__owners:
            return True
        return False

