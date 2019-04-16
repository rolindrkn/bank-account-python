'''
Created on Apr 14, 2019
Test for program, minimal test cases on top
@author: rolindrkn
'''
import unittest
from Customer import Customer
from Account import Account
from Account import Joint
from Transaction import Transaction


class TestCases(unittest.TestCase):
    USD = 2
    MXN = .1

    #Case 1:  Customer: Stewie Griffin Customer ID: 777 Account Number: 1234 
    #Initial Balance for account number 1234: $100.00 CAD  
    def test_case1(self):
        stewie = Customer(777, "Stewie Griffin")
        sAcc = stewie.trans.openChecking(1234, 100)
        
        
        #Stewie Griffin deposits $300.00 USD to account number 1234.  
        stewie.trans.deposit(sAcc, "300 USD")
        self.assertEqual(sAcc.getBalance(), 100+300*self.USD)
        
        print("Output1: " + sAcc.printBalance())
    
    #Case 2:  Customer: Glenn Quagmire Customer ID: 504 Account Number: 2001 
    #Initial balance for account number 2001: $35,000.00 CAD  
    def test_case2(self):
        quagmire = Customer(504, "Glen Quagmire")
        qAcc = quagmire.trans.openChecking(2001, 35000)
        
        #Glenn Quagmire withdraws $5,000.00 MXN from account number 2001. 
        quagmire.trans.withdraw(qAcc, "5000 MXN")
        self.assertEqual(qAcc.getBalance(), 35000-5000*self.MXN)
        
        #Glenn Quagmire withdraws $12,500.00 USD from account number 2001. 
        curBal = qAcc.getBalance()
        quagmire.trans.withdraw(qAcc, "12500 USD")
        self.assertEqual(qAcc.getBalance(), curBal-12500*self.USD)
        
        #Glenn Quagmire deposits $300.00 CAD to account number 2001. 
        curBal = qAcc.getBalance()
        quagmire.trans.deposit(qAcc, "300 CAD")
        self.assertEqual(qAcc.getBalance(), curBal+300)
        
        
        print("Output2: " + qAcc.printBalance())
    
    #Case 3:  Customer: Joe Swanson Customer ID: 002 Account Number: 1010 
    #Initial balance for account number 1010: $7,425.00 CAD
    def test_case3(self):
        joe = Customer("002", "Joe Swanson")
        jAcc = joe.trans.openChecking(1010, 7425)
        jAcc1 = joe.trans.openChecking(5500, 15000)
        
        #Joe Swanson withdraws $5,000.00 CAD from account number 5500.
        joe.trans.withdraw(jAcc1, "5000 CAD")
        self.assertEqual(jAcc1.getBalance(), 15000-5000)
         
        #Joe Swanson transfers $7,300.00 CAD from account number 1010 to account number 5500.
        curBal = jAcc.getBalance()
        curBal1 = jAcc1.getBalance()
        joe.trans.transfer(jAcc, jAcc1, "7300 CAD")
        self.assertEqual(jAcc.getBalance(), curBal-7300)
        self.assertEqual(jAcc1.getBalance(), curBal1+7300)
         
        #Joe Swanson deposits $13,726.00 MXN to account number 1010. 
        curBal = jAcc.getBalance()
        joe.trans.deposit(jAcc, "13726 MXN")
        self.assertEqual(jAcc.getBalance(), curBal+13726*self.MXN)        
        
        print("Output3: " + jAcc.printBalance() + " " + jAcc1.printBalance())
        
    #Case 4:  Customer: Peter Griffin Customer ID: 123 Account Number: 0123 
    #Initial balance for account number 0123: $150.00 CAD  
    #Customer: Lois Griffin Customer ID: 456 Account Number: 0456 
    #Initial balance for account number 0456: $65,000.00 CAD  
    def test_case4(self):
        peter = Customer(123, "Peter Griffin")
        lois = Customer(456, "Lois Griffin")
        pAcc = peter.trans.openChecking('0123', 150)
        lAcc = lois.trans.openChecking('0456', 65000)
        
        #Peter Griffin withdraws $70.00 USD from account number 0123. 
        peter.trans.withdraw(pAcc, "70 USD")
        self.assertEqual(pAcc.getBalance(), 150-70*self.USD)
        
        #Lois Griffin deposits $23,789.00 USD to account number 0456. 
        lois.trans.deposit(lAcc, "23789 USD")
        self.assertEqual(lAcc.getBalance(), 65000+23789*self.USD)
        
        #Lois Griffin transfers $23.75 CAD from account number 0456 to 
        #Peter Griffin (account number 0123).
        curpAcc = pAcc.getBalance()
        curlAcc = lAcc.getBalance()   
        lois.trans.transfer(lAcc, pAcc, "23.75 CAD")
        self.assertEqual(pAcc.getBalance(), curpAcc+23.75)
        self.assertEqual(lAcc.getBalance(), curlAcc-23.75)
        
        print("Output4: " + pAcc.printBalance() + " " + lAcc.printBalance())
    
    #Case 5: Customer: Joe Swanson Customer ID: 002 Account Number: 1010 
    #Initial balance for account number 1010: $7,425.00 CAD 
     
    #Famous social engineer and thief John Shark (Customer ID 219) attempts to 
    #withdraw $100 USD from account 1234.  
 
    def test_case5(self):
        joe = Customer("002", "Joe Swanson")
        jAcc = joe.trans.openChecking(1010, 7425)
        shark = Customer(219, "John Shark")
        
        #The bank determines that the account is not Johns and refuses to give him 
        #the money.
        shark.trans.withdraw(jAcc, "100 USD")
        self.assertEqual(jAcc.getBalance(), 7425)
        
        print("Output5: " + jAcc.printBalance())

    #######################################################
    #  Account Class                                      #
    #######################################################

    def test_Account(self):
        #special bal < 0
        acc = Account(1, -2, 1)
        self.assertEqual(acc.getActNo(), '1')
        self.assertEqual(acc.getBalance(), 0)
        
        #boundary bal = 0
        acc = Account('1', 0, '1')
        self.assertEqual(acc.getActNo(), '1')
        self.assertEqual(acc.getBalance(), 0)
        
        #boundary bal > 0
        acc = Account('abc', 10, '1')
        self.assertEqual(acc.getActNo(), 'abc')
        self.assertEqual(acc.getBalance(), 10)
        
        #boundary bal not number
        with self.assertRaises(TypeError):
            acc = Account(1, '10')
            
    #returns custId of account holder
    def test_getOwner(self):
        #boundary owner is an ID ie. number
        acc = Account(1, 10, 1234)
        owner = acc.getOwner()
        self.assertEqual(owner, '1234')

    # check if user is owner
    def test_isOwner(self):
        #boundary - is owner
        acc = Account(1, 10, 1234)
        owner = acc.getOwner()
        self.assertEqual(owner, '1234')
        
        #boundary - not owner
        acc = Account(1, 10, 1234)
        swner = acc.getOwner()
        self.assertNotEqual(owner, '12345')   
        
        #boundary - not owner
        acc = Account(1, 10, 1234)
        owner = acc.getOwner()
        self.assertNotEqual(owner, 'abc')   
        
    def test_deposit(self):
        #######################################################
        #               1 = 1 CAD                             #
        #######################################################
        #special amount < 0
        acc = Account(1, 10, 1)
        acc.deposit('-3 CAD')
        self.assertEqual(acc.getBalance(), 10.00)
        
        #boundary amount = 0.25   
        acc = Account(1, 10, 1)
        acc.deposit('0.25 CAD') 
        self.assertEqual(acc.getBalance(), 10.25)
        
        #boundary amount = 1
        acc.deposit('1 CAD') 
        self.assertEqual(acc.getBalance(), 11.25)
        
        #boundary amount = double
        acc.deposit('1.50 CAD') 
        self.assertEqual(acc.getBalance(), 12.75)
        
        #boundary amount = 50.20
        acc = Account(1, 10, 1)
        acc.deposit('50.20 CAD')
        self.assertEqual(acc.getBalance(), 60.20)
        
        #boundary amount = 50
        acc = Account(1, 10, 1)
        acc.deposit('50 CAD')
        self.assertEqual(acc.getBalance(), 60.00)
    
        #########################################################
        #    USD = 2 CAD                                        #
        #########################################################          
        #special amount < 0 USD 
        acc = Account(1, 10, 1)
        acc.deposit('-50 USD')
        self.assertEqual(acc.getBalance(), 10)
        
        #special amount = 0 USD 
        acc = Account(1, 10, 1)
        acc.deposit('0 USD')
        self.assertEqual(acc.getBalance(), 10)
        
        #boundary 0 USD < amount > 1 USD
        acc = Account(1, 10, 1)
        acc.deposit('0.25 USD')
        self.assertEqual(acc.getBalance(), 10+ .25*self.USD)
        
        #boundary amount = 1 USD
        acc = Account(1, 10, 1)
        acc.deposit('1 USD')
        self.assertEqual(acc.getBalance(), 10 + self.USD)
        
        #boundary amount = double
        acc = Account(1, 10, 1)
        acc.deposit('1.12 USD')
        self.assertEqual(acc.getBalance(), 10+(1.12*self.USD))
        
        #boundary amount = 51.20
        acc = Account(1, 10, 1)
        acc.deposit('51.20 USD')
        self.assertEqual(acc.getBalance(), 10+(51.20*self.USD))
    
    
        #########################################################
        #       MXN = .1 CAD                                   #
        #########################################################
        #special amount < 0 MXN 
        acc = Account(1, 10, 1)
        acc.deposit('-50 MXN')
        self.assertEqual(acc.getBalance(), 10)
        
        #special amount = 0 MXN 
        acc = Account(1, 10, 1)
        acc.deposit('0 MXN')
        self.assertEqual(acc.getBalance(), 10)
        
        #boundary 0 MXN < amount > 1 MXN
        acc = Account(1, 10, 1)
        acc.deposit('0.25 MXN')
        self.assertEqual(acc.getBalance(), 10+0.25*self.MXN)
        
        #boundary amount = 1 MXN
        acc = Account(1, 10, 1)
        acc.deposit('1 MXN')
        self.assertEqual(acc.getBalance(), 10 + self.MXN)
        
        #boundary amount = double
        acc = Account(1, 10, 1)
        acc.deposit('1.12 MXN')
        self.assertEqual(acc.getBalance(), 10+(1.12*self.MXN))
        
        #boundary amount = 51.20
        acc = Account(1, 10, 1)
        acc.deposit('51.20 MXN')
        self.assertEqual(acc.getBalance(), 10+(51.20*self.MXN))
        
    def test_withdraw(self):
        #special amount < 0
        acc = Account(1, 10, 1)
        result = acc.withdraw('-1 CAD')
        self.assertEqual(acc.getBalance(), 10)
        self.assertEqual(result, False)
        
        #special amount = 0
        acc = Account(1, 10, 1)
        result = acc.withdraw('0 CAD')
        self.assertEqual(acc.getBalance(), 10)
        self.assertEqual(result, False)
        
        #special amount > balance
        acc = Account(1, 10, 1)
        result = acc.withdraw('11 CAD')
        self.assertEqual(acc.getBalance(), 10)
        self.assertEqual(result, False)
        
        #boundary amount > 0 AND amount < bal
        acc = Account(1, 10, 1)
        result = acc.withdraw('1 CAD')
        self.assertEqual(acc.getBalance(), 9)
        self.assertEqual(result, True)
        
        #boundary amount = balance
        acc = Account(1, 10, 1)
        result = acc.withdraw('10 CAD')
        self.assertEqual(acc.getBalance(), 0)
        self.assertEqual(result, True)

        #########################################################
        #       MXN = .1 CAD                                    #
        #########################################################        
        #boundary amount = 1.40 MXN
        acc = Account(1, 10, 1)
        result = acc.withdraw('1.40 MXN')
        self.assertEqual(acc.getBalance(), 10 - 1.40*self.MXN)
        self.assertEqual(result, True)
        
        #special amount in MXN > bal
        acc = Account(1, 10, 1)
        result = acc.withdraw('100.20 MXN')
        self.assertEqual(acc.getBalance(), 10)
        self.assertEqual(result, False)
        
        #boundary amount in MXN = bal
        acc = Account(1, 10, 1)
        result = acc.withdraw('100 MXN')
        self.assertEqual(acc.getBalance(), 10 - 100*self.MXN)
        self.assertEqual(result, True)

        #########################################################
        #       USD = 2 CAD                                    #
        #########################################################
        #boundary amount < balance
        acc = Account(1, 10, 1)
        result = acc.withdraw('1.10 USD')
        self.assertEqual(acc.getBalance(), 10 - 1.10*self.USD)
        self.assertEqual(result, True)
        
        #special amount in USD > bal
        acc = Account(1, 10, 1)
        result = acc.withdraw('5.20 USD')
        self.assertEqual(acc.getBalance(), 10)
        self.assertEqual(result, False)
        
        #boundary amount in USD = bal
        acc = Account(1, 10, 1)
        result = acc.withdraw('5 USD')
        self.assertEqual(acc.getBalance(), 10 - 5*self.USD)
        self.assertEqual(result, True)


    #######################################################
    #  Joint Class                                        #
    #######################################################    
    def test_addOwner(self):
        #add 1 owner
        jAcc = Joint(124, 980, 982)
        jAcc.add_owner(194)
        self.assertEqual({'982', '194'}, jAcc.getOwners())
        
        #add 1 owner - not int
        jAcc = Joint(124, 980, 982)
        jAcc.add_owner('abc')
        self.assertEqual({'982', 'abc'}, jAcc.getOwners())
        
        #add 2 owner
        jAcc = Joint(124, 980, 982)
        jAcc.add_owner(194)
        jAcc.add_owner('80')
        self.assertEqual({'982', '194', '80'}, jAcc.getOwners())
        
        #owner already in list
        jAcc = Joint(124, 980, 982)
        jAcc.add_owner(194)
        jAcc.add_owner(80)
        jAcc.add_owner(80)
        self.assertEqual({'982', '194', '80'}, jAcc.getOwners())
        
    def test_getOwners(self):
        #one owner
        jAcc = Joint(124, 980, 982)
        self.assertEqual({'982'}, jAcc.getOwners())
        
        #multiple owners
        jAcc = Joint(124, 980, 982)
        jAcc.add_owner(194)
        jAcc.add_owner(80)
        self.assertEqual({'982', '194', '80'}, jAcc.getOwners())
            
    def test_removeOwners(self):
        #one owner
        jAcc = Joint(124, 980, 982)
        jAcc.remove_owner(982)
        self.assertEqual(set(), jAcc.getOwners())
        
        #multiple owners
        jAcc = Joint(124, 980, 982)
        jAcc.add_owner(194)
        jAcc.add_owner(80)
        jAcc.remove_owner(194)
        self.assertEqual({'982', '80'}, jAcc.getOwners())
        
        #not in set
        jAcc = Joint(124, 980, 982)
        jAcc.remove_owner(194)
        self.assertEqual({'982'}, jAcc.getOwners())
    
    def test_isOwnerJoint(self):
        #in the set
        jAcc = Joint(124, 980, 982)
        self.assertTrue(jAcc.isOwner(982))
        
        #in a set larger than 1
        jAcc = Joint(124, 980, 982)
        jAcc.add_owner(194)
        jAcc.add_owner(80)
        self.assertTrue(jAcc.isOwner(80))
        
        #not in a set
        jAcc = Joint(124, 980, 982)
        jAcc.add_owner(194)
        jAcc.add_owner(80)
        self.assertFalse(jAcc.isOwner(79))                 
        
        #not in empty set
        jAcc = Joint(124, 980, 982)
        jAcc.remove_owner(982)
        self.assertFalse(jAcc.isOwner(79)) 
        
        #not in set with size 1
        jAcc = Joint(124, 980, 982)
        self.assertFalse(jAcc.isOwner(79))       
        
        #not in set with userID not an int
        jAcc = Joint(124, 980, 982)
        self.assertFalse(jAcc.isOwner('abc')) 
        
    #######################################################
    #  Transaction Class                                  #
    #######################################################
    def test_openChecking(self):
        trans = Transaction(777)
        sAcc = trans.openChecking(1234, 100)
        self.assertEqual('1234', sAcc.getActNo())
        self.assertEqual(100, sAcc.getBalance())
        self.assertEqual('777', sAcc.getOwner())
    
    def test_openJoint(self):
        trans = Transaction(777)
        sAcc = trans.openJoint(1234, 100)
        self.assertEqual('1234', sAcc.getActNo())
        self.assertEqual(100, sAcc.getBalance())
        self.assertEqual({'777'}, sAcc.getOwners())

    def test_withdrawTransaction(self): 
        
        #######################################################
        #  CAD                                                #
        #######################################################
        first = Account("1234", 100, "777")
        sec = Joint("0123", 123, "150")
        sec.add_owner(777)  
        trans = Transaction(first.getOwner())
        
        #amt < bal (CAD)
        initBal = first.getBalance()
        trans.withdraw(first, "21.33 CAD")
        self.assertEqual(first.getBalance(), initBal - 21.33)
        
        #amt > bal (CAD)
        initBal = first.getBalance()
        trans.withdraw(first, "105 CAD")
        self.assertEqual(first.getBalance(), initBal)
        
        #amt < 0 (CAD)
        initBal = first.getBalance()
        trans.withdraw(first, "-105 CAD")
        self.assertEqual(first.getBalance(), initBal)       
        
        #amt = bal (CAD)
        initBal = first.getBalance()
        trans.withdraw(first, str(initBal) + " CAD")
        self.assertEqual(first.getBalance(), 0)        
        
        #owner of Joint, amt < bal(CAD)
        initBal = sec.getBalance()
        trans.withdraw(sec, "21.33 CAD")
        self.assertEqual(sec.getBalance(), initBal - 21.33)

        #owner of Joint, amt < 0
        initBal = sec.getBalance()
        trans.withdraw(sec, "-21.33 CAD")
        self.assertEqual(sec.getBalance(), initBal)
        
        #owner of Joint, amt < bal(CAD)
        initBal = sec.getBalance()
        trans.withdraw(sec, "210.33 CAD")
        self.assertEqual(sec.getBalance(), initBal)
        
        #owner of Joint, amt = bal(CAD)
        initBal = sec.getBalance()
        trans.withdraw(sec, str(initBal) + " CAD")
        self.assertEqual(sec.getBalance(), 0)  
        
        #######################################################
        #  USD                                                #
        #######################################################
        USD = 2
        first = Account("1234", 1023.41, "777")
        sec = Joint("0123", 123.99, "150")
        sec.add_owner(777)  
        trans = Transaction(first.getOwner())
        
        #amt < bal (USD)
        initBal = first.getBalance()
        trans.withdraw(first, "21.33 USD")
        self.assertEqual(first.getBalance(), initBal - 21.33* USD)
        
        #amt > bal (USD)
        initBal = first.getBalance()
        trans.withdraw(first, "50000 USD")
        self.assertEqual(first.getBalance(), initBal)
        
        #amt < 0 (USD)
        initBal = first.getBalance()
        trans.withdraw(first, "-105 USD")
        self.assertEqual(first.getBalance(), initBal)       
        
        #amt = bal (USD)
        initBal = first.getBalance()
        trans.withdraw(first, str(initBal/USD) + " USD")
        self.assertEqual(first.getBalance(), 0)        
        
        #owner of Joint, amt < bal(USD)
        initBal = sec.getBalance()
        trans.withdraw(sec, "21.33 USD")
        self.assertEqual(sec.getBalance(), initBal - 21.33*USD)

        #owner of Joint, amt < 0
        initBal = sec.getBalance()
        trans.withdraw(sec, "-21.33 USD")
        self.assertEqual(sec.getBalance(), initBal)
        
        #owner of Joint, amt > bal(USD)
        initBal = sec.getBalance()
        trans.withdraw(sec, "210.33 USD")
        self.assertEqual(sec.getBalance(), initBal)
        
        #owner of Joint, amt = bal(CAD)
        initBal = sec.getBalance()
        trans.withdraw(sec, str(initBal/2) + " USD")
        self.assertEqual(sec.getBalance(), 0)  
        
        #######################################################
        #  MXN                                                #
        #######################################################
        MXN = .1
        first = Account("1234", 102.41, "777")
        sec = Joint("0123", 123.99, "150")
        sec.add_owner(777)  
        trans = Transaction(first.getOwner())
        
        #amt < bal (MXN)
        initBal = first.getBalance()
        trans.withdraw(first, "21.33 MXN")
        self.assertEqual(first.getBalance(), initBal - 21.33* MXN)
        
        #amt > bal (MXN)
        initBal = first.getBalance()
        trans.withdraw(first, "500000 MXN")
        self.assertEqual(first.getBalance(), initBal)
        
        #amt < 0 (MXN)
        initBal = first.getBalance()
        trans.withdraw(first, "-105 MXN")
        self.assertEqual(first.getBalance(), initBal)       
        
        #amt = bal (MXN)
        initBal = first.getBalance()
        trans.withdraw(first, str(initBal/MXN) + " MXN")
        self.assertEqual(first.getBalance(), 0)        
        
        #owner of Joint, amt < bal(MXN)
        initBal = sec.getBalance()
        trans.withdraw(sec, "21.33 MXN")
        self.assertEqual(sec.getBalance(), initBal - 21.33*MXN)

        #owner of Joint, amt < 0
        initBal = sec.getBalance()
        trans.withdraw(sec, "-21.33 MXN")
        self.assertEqual(sec.getBalance(), initBal)
        
        #owner of Joint, amt > bal(MXN)
        initBal = sec.getBalance()
        trans.withdraw(sec, "2100000.33 MXN")
        self.assertEqual(sec.getBalance(), initBal)
        
        #owner of Joint, amt = bal(CAD)
        initBal = sec.getBalance()
        trans.withdraw(sec, str(initBal/MXN) + " MXN")
        self.assertEqual(sec.getBalance(), 0)  
        
        #######################################################
        #  Not owner                                          #
        #######################################################
        first = Account("1234", 102.41, "777")
        sec = Joint("0123", 123.99, "150")
        sec.add_owner(777)  
        trans = Transaction(989)
        
        #checking
        initBal = first.getBalance()
        trans.withdraw(first, "21.33 MXN")
        self.assertEqual(first.getBalance(), initBal)
        
        #joint
        initBal = sec.getBalance()
        trans.withdraw(sec, str(initBal/MXN) + " MXN")
        self.assertEqual(sec.getBalance(), initBal)
    
    ##deposit into an account
    def test_depositTrans(self):
        first = Account("1234", 102.41, "777")
        sec = Joint("0123", 123.99, "150")
        sec.add_owner(777)  
        user = Transaction(150)

        #######################################################
        #               1 = 1 CAD                             #
        #######################################################
        #special amount < 0
        initBal = first.getBalance()
        user.deposit(first, "-1 CAD")
        self.assertEqual(first.getBalance(), initBal)
        
        initBal = sec.getBalance()
        user.deposit(sec, "-1 CAD")
        self.assertEqual(sec.getBalance(), initBal)
        
        #boundary amount = 4.25   
        initBal = first.getBalance()
        user.deposit(first, "4.25 CAD")
        self.assertEqual(first.getBalance(), initBal+4.25)
        
        initBal = sec.getBalance()
        user.deposit(sec, "4.25 CAD")
        self.assertEqual(sec.getBalance(), initBal+4.25)

        #sepcial amount = 0
        initBal = first.getBalance()
        user.deposit(first, "0 CAD")
        self.assertEqual(first.getBalance(), initBal)
        
        initBal = sec.getBalance()
        user.deposit(sec, "0 CAD")
        self.assertEqual(sec.getBalance(), initBal)
    
        #########################################################
        #    USD = 2 CAD                                        #
        #########################################################  
        USD= 2
        
        #special amount < 0
        initBal = first.getBalance()
        user.deposit(first, "-1 USD")
        self.assertEqual(first.getBalance(), initBal)
        
        initBal = sec.getBalance()
        user.deposit(sec, "-1 USD")
        self.assertEqual(sec.getBalance(), initBal)
        
        #boundary amount = 4.25   
        initBal = first.getBalance()
        user.deposit(first, "4.25 USD")
        self.assertEqual(first.getBalance(), initBal+4.25*USD)
        
        initBal = sec.getBalance()
        user.deposit(sec, "4.25 USD")
        self.assertEqual(sec.getBalance(), initBal+4.25*USD)

        #sepcial amount = 0
        initBal = first.getBalance()
        user.deposit(first, "0 USD")
        self.assertEqual(first.getBalance(), initBal)
        
        initBal = sec.getBalance()
        user.deposit(sec, "0 USD")
        self.assertEqual(sec.getBalance(), initBal)
    
        #########################################################
        #       MXN = .1 CAD                                   #
        #########################################################
        MXN = 0.1
        
        #special amount < 0
        initBal = first.getBalance()
        user.deposit(first, "-1 MXN")
        self.assertEqual(first.getBalance(), initBal)
        
        initBal = sec.getBalance()
        user.deposit(sec, "-1 MXN")
        self.assertEqual(sec.getBalance(), initBal)
        
        #boundary amount = 4.25   
        initBal = first.getBalance()
        user.deposit(first, "4.25 MXN")
        self.assertEqual(first.getBalance(), initBal+4.25*MXN)
        
        initBal = sec.getBalance()
        user.deposit(sec, "4.25 MXN")
        self.assertEqual(sec.getBalance(), initBal+4.25*MXN)

        #sepcial amount = 0
        initBal = first.getBalance()
        user.deposit(first, "0 MXN")
        self.assertEqual(first.getBalance(), initBal)
        
        initBal = sec.getBalance()
        user.deposit(sec, "0 MXN")
        self.assertEqual(sec.getBalance(), initBal)
        
        
    def test_transfer(self):
        #######################################################
        #  CAD                                                #
        #######################################################
        first = Account("1234", 100, "777")
        sec = Joint("0123", 123, "150")
        sec.add_owner(777)  
        trans = Transaction(first.getOwner())
        
        #amt < bal (CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(first, sec, "20 CAD")
        self.assertEqual(first.getBalance(), initBal1 - 20)
        self.assertEqual(sec.getBalance(), initBal2 + 20)
        
        #amt > bal (CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(first, sec, str(initBal1+.1) + " CAD")
        self.assertEqual(first.getBalance(), initBal1)
        self.assertEqual(sec.getBalance(), initBal2)
        
        #amt < 0 (CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(first, sec, "-1.01 CAD")
        self.assertEqual(first.getBalance(), initBal1)
        self.assertEqual(sec.getBalance(), initBal2)     
        
        #amt = bal (CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(first, sec, str(initBal1) + " CAD")
        self.assertEqual(first.getBalance(), 0)
        self.assertEqual(sec.getBalance(), initBal2 + initBal1)        
        
        #owner of Joint, amt < bal(CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(sec, first, "100 CAD")
        self.assertEqual(first.getBalance(), initBal1 + 100)
        self.assertEqual(sec.getBalance(), initBal2 - 100) 

        #owner of Joint, amt < 0
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(sec, first, "-100 CAD")
        self.assertEqual(first.getBalance(), initBal1)
        self.assertEqual(sec.getBalance(), initBal2) 
        
        #owner of Joint, amt > bal(CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(sec, first, "1000000 CAD")
        self.assertEqual(first.getBalance(), initBal1)
        self.assertEqual(sec.getBalance(), initBal2) 
        
        #owner of Joint, amt = bal(CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(sec, first, str(initBal2)+ " CAD")
        self.assertEqual(first.getBalance(), initBal1 + initBal2)
        self.assertEqual(sec.getBalance(), 0) 
        
        #######################################################
        #  USD                                                #
        #######################################################
        USD = 2
        first = Account("1234", 100, "777")
        sec = Joint("0123", 123, "150")
        sec.add_owner(777)  
        trans = Transaction(first.getOwner())
        
        #amt < bal (CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(first, sec, "20 USD")
        self.assertEqual(first.getBalance(), initBal1 - 20*USD)
        self.assertEqual(sec.getBalance(), initBal2 + 20*USD)
        
        #amt > bal (CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(first, sec, str(initBal1+.1) + " USD")
        self.assertEqual(first.getBalance(), initBal1)
        self.assertEqual(sec.getBalance(), initBal2)
        
        #amt < 0 (CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(first, sec, "-1.01 USD")
        self.assertEqual(first.getBalance(), initBal1)
        self.assertEqual(sec.getBalance(), initBal2)     
        
        #amt = bal (CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(first, sec, str(initBal1/USD) + " USD")
        self.assertEqual(first.getBalance(), 0)
        self.assertEqual(sec.getBalance(), initBal2 + initBal1)        
        
        #owner of Joint, amt < bal(CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(sec, first, "10 USD")
        self.assertEqual(first.getBalance(), initBal1 + 10*USD)
        self.assertEqual(sec.getBalance(), initBal2 - 10*USD) 

        #owner of Joint, amt < 0
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(sec, first, "-100 USD")
        self.assertEqual(first.getBalance(), initBal1)
        self.assertEqual(sec.getBalance(), initBal2) 
        
        #owner of Joint, amt > bal(CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(sec, first, "1000000 USD")
        self.assertEqual(first.getBalance(), initBal1)
        self.assertEqual(sec.getBalance(), initBal2) 
        
        #owner of Joint, amt = bal(CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(sec, first, str(initBal2/USD)+ " USD")
        self.assertEqual(first.getBalance(), initBal1 + initBal2)
        self.assertEqual(sec.getBalance(), 0) 
        
        #######################################################
        #  MXN                                                #
        #######################################################
        MXN = .1
        first = Account("1234", 100, "777")
        sec = Joint("0123", 123, "150")
        sec.add_owner(777)  
        trans = Transaction(first.getOwner())
        
        #amt < bal (CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(first, sec, "20 MXN")
        self.assertEqual(first.getBalance(), initBal1 - 20*MXN)
        self.assertEqual(sec.getBalance(), initBal2 + 20*MXN)
        
        #amt > bal (CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(first, sec, str(initBal1/MXN+.1) + " MXN")
        self.assertEqual(first.getBalance(), initBal1)
        self.assertEqual(sec.getBalance(), initBal2)
        
        #amt < 0 (CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(first, sec, "-1.01 MXN")
        self.assertEqual(first.getBalance(), initBal1)
        self.assertEqual(sec.getBalance(), initBal2)     
        
        #amt = bal (CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(first, sec, str(initBal1/MXN) + " MXN")
        self.assertEqual(first.getBalance(), 0)
        self.assertEqual(sec.getBalance(), initBal2 + initBal1)        
        
        #owner of Joint, amt < bal(CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(sec, first, "10 MXN")
        self.assertEqual(first.getBalance(), initBal1 + 10*MXN)
        self.assertEqual(sec.getBalance(), initBal2 - 10*MXN) 

        #owner of Joint, amt < 0
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(sec, first, "-100 MXN")
        self.assertEqual(first.getBalance(), initBal1)
        self.assertEqual(sec.getBalance(), initBal2) 
        
        #owner of Joint, amt > bal(CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(sec, first, "1000000 MXN")
        self.assertEqual(first.getBalance(), initBal1)
        self.assertEqual(sec.getBalance(), initBal2) 
        
        #owner of Joint, amt = bal(CAD)
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(sec, first, str(initBal2/MXN)+ " MXN")
        self.assertEqual(first.getBalance(), initBal1 + initBal2)
        self.assertEqual(sec.getBalance(), 0) 
        
        #######################################################
        #  Not owner                                          #
        #######################################################
        first = Account("1234", 102.41, "777")
        sec = Joint("0123", 123.99, "150")
        sec.add_owner(777)  
        trans = Transaction("0123")
        
        #checking
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(first, sec, str(initBal2/MXN)+ " MXN")
        self.assertEqual(first.getBalance(), initBal1)
        self.assertEqual(sec.getBalance(), initBal2) 
        
        #joint
        initBal1 = first.getBalance()
        initBal2 = sec.getBalance()
        trans.transfer(sec, first, str(initBal2/USD)+ " USD")
        self.assertEqual(first.getBalance(), initBal1)
        self.assertEqual(sec.getBalance(), initBal2) 
    

    #######################################################
    #  Customer Class                                     #
    #######################################################
    def test_Customer(self):
        stewie = Customer('Stewie Griffin', 777)
        self.assertEqual('Stewie Griffin', stewie.getName())
        self.assertEqual('777', stewie.getID())
        
        jim = Customer(1234, 'abc')
        self.assertEqual('1234', jim.getName())
        self.assertEqual('abc', jim.getID())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCases']
    unittest.main()