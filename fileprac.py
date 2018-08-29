# File practice


with open('data/article.txt', 'a') as fobj:
    print('It has survived not only five centuries, but also the leap into electronic typesetting', file=fobj)
with open('data/binary', 'wb') as fobject:
    fobject.write(b'Life is good')



# Read a binary data file
with open('data/binary', 'rb') as fobj:
    content = fobj.read()
    content_decode = content.decode('utf-8')
    print(content_decode)

#file Exist Checking

import os
if os.path.exists('data/binarya'):
    print("File is exist")
else:
    print('file does not exist')

# Read CSV file

import csv 

with open('data/Data.csv', 'r') as fobj:
    fcsv = csv.reader(fobj)
    
    sum = 0
    for i, row in enumerate(fcsv):
        print (i, row[0], row[1])
        sum += int(row[1]) if i > 0 else 0
    print ("Total Cost: ", sum)

## CSV file write
# list_items   = [["name", 'age', 'country'],
#                 ['Bill Gates', 55, 'US'],
#                 ['Mark Zuckerberg', 34, 'US'],
#                 ['Swift', 35, 'Canada']
#                 ]

# import csv

# with open('data/people.csv', 'w') as fobj:
#     fcsv = csv.writer(fobj)
#     fcsv.writerows(list_items)
 




