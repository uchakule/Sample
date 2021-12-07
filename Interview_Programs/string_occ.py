a = '637289019282413131415171819'

class Umesh:
    def count():
        b = {}
        for i in a:
            if i in b:
                b[i]+=1
            else:
                b[i]=1 
        return b
T = Umesh.count()
print(T)


