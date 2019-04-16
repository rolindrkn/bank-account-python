'''
Created on Apr 14, 2019
Enumerator for CAD, USD, and MXN in terms of CAD
@author: Rosalind Ng
'''

from enum import Enum

class Currencies(Enum):
    '''
    1 CAD = 1 CAD
    1 USD = 0.5 CAD
    1 MXN = 10 CAD
    
    '''
    CAD = 1
    USD = 1/0.5
    MXN = 1/10
    
    @staticmethod
    def getValue(cur):
        #returns the exchange rate whne converted to CAD
        if cur == "CAD":
            return Currencies.CAD.value
        
        elif cur == "USD":
            return Currencies.USD.value
        
        else:
            return Currencies.MXN.value