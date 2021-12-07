"""
1. A decorator is a design pattern in Python that allows a user to add 
   new functionality to an existing object without modifying its structure.
2. Decorators are usually called before the definition of a function you want to decorate.   
"""
"example"

def dec2(func1):
    def run():
        print("Memory assigned....")
        func1()
        print("Job running completed....")
    return run   

@dec2
def job1():
    print("Job 1 is in progress now.....")

@dec2
def job2():
    print("Job 2 is in progress now....")    

job1()
job2()

"""3. Python allows a nested function to access the outer scope of the enclosing function. This is a critical concept in decorators 
-- this pattern is known as a Closure."""

def print_message(message):
    def message_sender():
        print(message)
    message_sender()

print_message('Hi Umesh')        