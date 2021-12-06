
#Parent Class
class User():
    def __init__(self,name,age,gender):
        self.name= name
        self.age = age
        self.gender = gender

    def user_details(self):
        """ Define class shows the user deatails """
        print('User details are :-')
        print('User Name :',self.name)
        print('User Age :',self.age)
        print('User Gender :',self.gender)

#Child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated :",self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if self.amount>self.balance:
            print("Insufficient balance can't withdraw balance | Available balance is",self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Balance withdraw successfully | Remaining balance is",self.balance)    

    def view_balance(self):
        self.user_details()
        print("Your Balance is",self.balance)


Umesh = Bank('Umesh',26,'Male')
Umesh.deposit(500)
Umesh.withdraw(300)
Umesh.view_balance()