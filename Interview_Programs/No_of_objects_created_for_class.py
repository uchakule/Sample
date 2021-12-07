class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def noOfobjects(cls):
        print('no of objects created for class',cls.count)
t1 = Test()
t2 = Test()
t3 = Test()
t4 = Test()
Test.noOfobjects()