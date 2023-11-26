a=10
b=12 
#print(type(b))

# print(a<b)
x=bool(9)
#print(x)
y=bool(0)
# print(y)
del a
del b
a='''ali
haoder
hamza
bashir'''
#print (a[-1])
#print(len(a))
#print('hsa'not in a)
del x
del y
item ='shirt'
qty=input("How many qty you want to buy ")
price=int(qty)*20

p1="I want {} {} "
print(p1.format(qty,item ))
print(f"Your total generated bill is {price}")
