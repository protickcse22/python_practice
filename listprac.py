import re
num_list = [1, 2, 3, 'my', 5.5, 4]
sum = 0
for i in num_list:
    if type(i) == int:
        sum += i
print('Summation= {sum}'.format(sum=sum))
print(num_list[3:])
num_list[1]=5
print(num_list)
#numstr=' '.join(num_list)
#num_list.sort(reverse=True)
print(num_list)

print(num_list[0:3])
num_list+=['10']
print(num_list)
num_list.insert(3,22)
print(num_list)

lst=[2,4,1,8,4,8]
lst.sort()
print(lst)

