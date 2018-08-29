# def div(x,y):
#     try:
#         res=x/y
#     except Exception as e:
#         print("Exceptation name:  ",e,"Exception")
#         return None
#     return res

# print(div(2,0))
# print(div(4,2))
# print(div('2',2))


# Creating custom exception
class VowelNotExcepted(Exception):
    def __init__(self,message,status):
        super().__init__(message,status)
        self.message=message
        self.status=status

def checkCar(word):
    for char in word:
        if char.lower() in ['a','e','i','o','u']:
            raise VowelNotExcepted("vowel is not excepted",101)
    return word

try:
   print(checkCar('love')) 
except Exception as e:
    print("Eeception is: ",e)
finally: 
    print('Hello')   
