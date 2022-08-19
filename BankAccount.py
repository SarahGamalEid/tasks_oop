class BankAccount:
    def __init__(self,accountNumber,name ,balance):
        self.accountNumber=accountNumber #public
        self.name=name #public
        self.__balance = balance  # private

    def get_balance(self):
        return self.__balance


    def set_balance(self, balance):
            self.__balance = balance

    def Deposit(self,deposit_money):
        self.__balance =deposit_money + self.__balance
        #return self.__balance

    def Withdrawal(self,withdrawal_money):
        if (self.__balance < withdrawal_money):
            print("impossible operation! Insufficient balance !")
        else:
            self.__balance =self.__balance - withdrawal_money

    def bankFees(self):
        self.__balance=self.__balance * (95/100)
        #self.__balance = self.__balance - fees
        #print("bank fees : ",fees)
        #self.__balance = self.__balance * (95/100)
        #print("balance after deducting fees : ")
        return self.__balance 

    def display(self):
        print("Account Number : ", self.accountNumber)
        print("Account Name : ", self.name)
        print("Account Balance : ", self.__balance, " $")


# Testing the code :
Account_1 = BankAccount(12345, "ahmed" , 1000)
# Creating Withdrawal Test
Account_1.Withdrawal(300)
# Create deposit test
Account_1.Deposit(200)
# Display account informations
Account_1.display()


