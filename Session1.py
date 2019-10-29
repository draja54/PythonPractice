# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
price = 49
txt = "The price is {1:.4f} dollars"
print(txt.format("",price))

txt = "I have a {carname}, It is a {carmodel}"
print(txt.format(carname = "FORD", carmodel="Mustang"))

y = "abc123"
z = "abc123a"
x = y

print(x is not z)



# List
a = ['1','2','3','4','4']
for x in a:
    print(x)
    
if "1" not in a:
    print("Yes")
else:
    print("No")
    
a[4] = 'Naveena'

print(a[4])
for x in a:
    print(x)
    
txt = "length of the list {}"
print(txt.format(len(a)))

a.append("Raja")

for x in a:
    print(x)
    
a.insert(2,"Apple")
print(a)

a.remove("Apple")

print(a)
a.pop()

print(a)

a.pop(2)
print(a)


del a[3]
print(a)

a.clear()
print(a)

b = ['1','2','3','4','4']
print(b)

del b
#print(b)


b = ['1','2','3','4','4']
print(b)
c = list(b)
print(c)

d = b.copy()
print(d)

e = list(('1','2','3','4','4'))
print(e)

#tuple
tup_a = ('a','b','c')
print(tup_a)

print(tup_a.index('c'))
print(tup_a.count('c'))

