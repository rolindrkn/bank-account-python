'''
Created on Apr 14, 2019

@author: rolindrkn
'''
from Transaction import Transaction

class Customer:
    '''
    Creates a customer including name and id
    '''
    
    def __init__(self, name, iD):
        self.__name = str(name)
        self.__iD = str(iD)
        self.trans = Transaction(self.__iD)
        
    def getName(self):
        #returns customer name
        return self.__name
    
    def getID(self):
        #returns customer Id
        return self.__iD