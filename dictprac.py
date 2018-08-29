price_list={

    'rice':20,
    'dall':45,
    'sugar':15,
    'fish':200
}

print(price_list['dall'],'|',price_list['sugar'])
del price_list['dall']
print(price_list)
price_list['dall']=45
print(price_list)

for key in sorted(price_list.keys(),reverse=True):
    print(key,price_list[key])
    