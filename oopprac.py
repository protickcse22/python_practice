# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __del__(self):
#         print(self.name+ " is Destroyed")
#     def details(self):
#         print(self.name,self.age,sep="---")
# persion_list=[]
# for i in range(0,3):
#     person=Person("Person "+str(i),30+i)
#     persion_list+=[person]

# for x in persion_list:
#     x.details()


# Inheritence
class Math: # Parent class
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def sum(self):
        return self.x + self.y 
        
class MathExtended1 (Math): # Child class
    def __init__(self, x, y):
        super().__init__(x, y) # super() func makes connection to parent class with child class
        
    def subtract(self):
        return self.x - self.y 
        
math_obj = Math(2, 4)
print ( math_obj.sum() )

math_ext_obj = MathExtended1(10, 2)
print ( math_ext_obj.subtract() )

