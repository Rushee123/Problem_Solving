class Fraction():
    def __init__(self,num,dnum):
        self.num = num
        self.dnum = dnum

    def __str__(self):
        return "{}/{}".format(self.num,self.dnum)

    def __add__(self, other):
        num = self.num*other.dnum + self.dnum*other.num
        dnum = self.dnum*other.dnum
        return "{}/{}".format(num,dnum)
    def __sub__(self, other):
        num = self.num*other.dnum - self.dnum*other.num
        dnum = self.dnum*other.dnum
        return "{}/{}".format(num,dnum)
    def __mul__(self, other):
        num = self.num*other.num
        dnum = self.dnum*other.dnum
        return "{}/{}".format(num,dnum)
    def __truediv__(self, other):
        num = self.num*other.dnum
        dnum = self.dnum*other.dnum
        return "{}/{}".format(num,dnum)




a = Fraction(4,5)
b=  Fraction(4,8)
print("sum===",a+b)
print("sub===",a-b)
print("mul===",a*b)
print("div==",a/b)



print(a)


