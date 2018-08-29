
'''
All String method
practice
'''
name = '   Mr. X Rahman     '
print('_'+name.strip()+'_')

text='Hello World'
print(text.split())


# for x in text:
#     print(x)

matrix=[
    [1,2,3,4,5],
    [6,7,2,3,4],
    [44,3,5,6]
]
for i in matrix:
    for j in i:
        print(j,end=' ')
    print() 
# String title,upper,split,replace function practice      
title='hello brother'
print(title.title().upper().split())
print(title.replace('brother','sister'))

#String interpolation
name='Jodu'
print('Your name is {name}'.format(name=name))


















# class Hello:
#     def show(self,text):
#         print("Your Message = ",text)


# # x = Hello()
# # x.show("Hello world")

# obj=[]

# for i in range(4):
#     obj[i] = Hello()
# # obj[1].show("Dummy text")
# # obj[2].show("Another Dummy text")
# print("Hello")
