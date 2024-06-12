class Student:
    def marks(self,m1,m2,m3,m4):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
    def avg(self):
        average = (self.m1+self.m2+self.m3+self.m4)/4
        print(average)
obj = Student()
obj.marks(100,87,67,98)
obj.avg()