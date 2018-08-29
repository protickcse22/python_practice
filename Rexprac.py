import re
# date_data='10/Jul/2018 is your birthday'
# if re.match(r'\d+/[a-zA-z]+/\d{4}',date_data):
#     print('Matched')
# else:
#     print('Missmatched') 

# # Compling pattern for reuse

# date_data='10/Jul/2018 is your birthday'
# complied_data=re.compile(r'\d+/[a-zA-z]+/\d{4}')
# if  complied_data.match(date_data):
#     print('Matched')
# else:
#     print('Missmatched') 

# #Capture Group
# date_data='10/Jul/2018 is your birthday'
# complied_data=re.compile(r'(\d+)/([a-zA-z]+)/(\d{4})')
# result=complied_data.match(date_data)
# for i in range(0,4):
#     print(result.group(i))
# print(result.groups())
# x,y,z=result.groups()
# print('Day is: ',x)


#Capltal Letter of Month

date_data='10/Jul/2018 is your birthday'
complied_data=re.compile(r'(\d+)/([a-zA-z]+)/(\d{4})')

def toUpper(m):
    return '{} {} {}'.format(m.group(3),m.group(2).upper(),m.group(1))
new_srt=complied_data.sub(toUpper,date_data)
print(new_srt)

# Case Insensitive search

text = "I am GOOD, but I am NOt very good"
list = re.findall('good', text, flags=re.IGNORECASE)
print (list)
text = re.sub('gOOd', 'bad', text, flags=re.IGNORECASE)
print (text)
