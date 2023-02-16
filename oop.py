class eMobilisstudents:
    def __init__(self, name , age):
      self.name= name
      self.age=age
    def hello_me(self):
        print(f"my name is {self.name} and am {self.age} years old")
#creating an object
myobj=eMobilisstudents("Victor",30)
myobj.hello_me()

class high_school:
    def __init__(self,name,schhol):
        self.name=name
        self.school=high_school
    def addmittion(self):
        print(f"hi {self.name} you are addmite to{self.school}by thursday")
myobj=high_school("Nick","Kiambu")
myobj.addmittion()

# creat a class called magari it should have a mode, make, year, properties
class magari:
    def __init__(self,mode,make,year):
        self.mode=mode
        self.make=make
        self.year=year
    def varieties(self):
        print(f"we sell {self.mode};{self.make},{self.year}")
myobj=magari("Toyota", "cvc", 2020)
myobj.varieties()

# scholl class
class school:
    def __init__(my,name,form):
        my.name=name
        my.form=form
    def adm(my):
        print(f"welcome {my.name} you are addmited to form {my.form}")
myobj=school("Victor",4)
myobj.adm()

