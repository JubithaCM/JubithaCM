class flower:
    def __init__(self):
        self.name=input("Enter flowername")
    def display(self):
        if hasattr(self,'petalcolor'):
            print("Flower name:",self.name,"Petal color:",self.petalcolor)
             
        else:
            print("Unknown flower")
f=flower()
f.display()
setattr(f,'petalcolor','yellow')
f.display()
