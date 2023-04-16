#class Person:
   # def __init__(self,name,age):
  #      self.name= name
    #    self.age= age
    #def displayPerson(self):
        #print("Person: "+ self.name + ","+str(self.age))
class Student:
    def __init__(self,name,age,grade):
        self.name= name
        self.age= age
        self.grade= grade
    def displayStudent(self):
        print("Person: "+ self.name + ","+str(self.age)+","+self.grade)
        #print(self.grade)
class Teacher:
    def __init__(self,name,age,course):
        self.name= name
        self.age= age
        self.course= course
    def displayTeacher(self):
        print("Person: "+ self.name + ","+str(self.age)+","+self.course)   
        #print(self.course)
    
