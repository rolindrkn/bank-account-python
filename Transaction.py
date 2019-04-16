'''
Created on Apr 14, 2019
Transaction that is allowed by a customer at a bank
@author: rosalind Ng
'''
from Account import Checking
from Account import Joint

class Transaction(object):
    '''
    Transaction that is allowed by a customer at a bank
    '''
    def __init__(self, user):
        self.__user = user
    
    def openChecking(self, accNo, initBal):
        #opens a checking account
        return Checking(accNo, initBal, self.__user)
    
    def openJoint(self, accNo, initBal):
        #opens a joint account with inicial customer      
        return Joint(accNo, initBal, self.__user) 

    def transfer(self, fromAct, toAct, amount):
        #transfer money from one account to another if user 
        #is the owner of the source account     
        if fromAct.isOwner(self.__user):
            if fromAct.withdraw(amount):
                self.deposit(toAct, amount)

    def withdraw(self, act, amount):  
        #withdraw from an account, if user is owner of account
        if act.isOwner(self.__user):
            act.withdraw(amount)

    def deposit(self, act, amount):
        #deposit into an account
        act.deposit(amount)
            