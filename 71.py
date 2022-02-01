class rectangle:
    def __init__(self):
        self.len=int(input("Enter  length"))
        self.bd=int(input("Enter  breadth"))
    def area(self):
        return self.len*self.bd
    def perimeter(self):
        return 2*(self.len+self.bd)
try:
 r=rectangle()
 print("Area of Rectangle is",r.area())
 print("Perimeter of Rectangle is",r.perimeter())
except Exception as e:
    print(e)
