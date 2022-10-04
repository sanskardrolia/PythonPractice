# #public
class Person:
    name=None
    age=None
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_detail(self):
        print("Name: {0} and Age: {1}".format(self.name,self.age))
obj=Person("Sanskar",21)
obj.display_detail()
print("Age access publically: ",obj.age)

# #protected
class Hero:
    _name=None
    _age=None
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def Details(self):
        print("Name : {0} Age: {1}".format(self._name,self._age))
#derived class
class Movie(Hero):
    def __init__(self,name,age):
        Hero.__init__(self,name,age)
    def diplay_detail(self):
        print("Name : {0}".format(self._name))
        self.Details()
obj2=Movie("Jay",24)
obj2.diplay_detail()

#private
class ask:
    __name=None
    __age=None
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def display_detail(self):
        print("Name: {0} and Age: {1}".format(self.__name,self.__age))
    def accessPrivate(self):
        self.display_detail()
obj3=ask("Sanskar",21)
obj3.accessPrivate()
#game over;;;;;