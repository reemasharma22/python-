class Dog:
    energy = "high"

    def speak(self):
        print("woof")

bilbo_waggins = Dog()
print(bilbo_waggins.energy)
bilbo_waggins.speak()

#useof_init_

class Dog:
    energy = "high"

    def speak(self):
        print("woof")

bilbo_waggins = Dog()
print(bilbo_waggins.energy)
bilbo_waggins.speak()

#Example

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

John = Student("John", "21")
Jane = Student("Jane", "22")

print(getattr(John, "age"))

#Classchallenge 

class Student():
    class = "Student"
    def __init__(self,name,age,score1,score2,score3):
        self.name = name
        self.age = age
        self.score1 = score1
        self.score2 = score2 
        self.score3 = score3

    def calcAverage(self):
        return int(slef.score1 + self.score2 + self.score3)/3

John = student ("johnn","23",70,5,67,8,80,56)
print(john.calcAverage())