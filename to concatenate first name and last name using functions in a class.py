from fnmatch import fnmatch

class A:
    def getName(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def display(self):
        print(self.fname + self.lname)
obj = A()
obj.getName("John","Wick")
obj.display()