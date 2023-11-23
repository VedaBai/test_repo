a=1
b=0
c=None
try:
    c=a/b
except ZeroDivisionError:
    print("I got exception for zero division but let me proceed")
except TypeError:
    print("I got exception for type error but let me proceed")
except:
    print("I got some exception but let me proceed")
finally:
    print("final block")
print(c)

from abc import ABC, abstractmethod
class Car(ABC):

    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def steering(self):
        pass

    @abstractmethod
    def tyre(self):
        pass

    @abstractmethod
    def gearbox(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

class BMW(Car):


    def engine(self):
        pass

    def steering(self):
        pass

    def tyre(self):
        pass

    def gearbox(self):
        pass

    def fuel_type(self):
        pass



class Human:

    def __init__(self,name,sex,qualification):
        self.human_name = name
        self.human_sex = sex
        self.human_qualification = qualification


R = Human("veda", "female", "B.E")
print(R.human_name)
print(R.human_sex)
print(R.human_qualification)