class MyClass():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s = a*b
        else:
            s='Provide atleast two numbers'
        return s
obj = MyClass()
print(obj.sum(10,20,30))


# class MyClass():
#     def add(self,a,b):
#         print(a+b)
# obj = MyClass()
# print(obj.add('Umesh','Mayur'))