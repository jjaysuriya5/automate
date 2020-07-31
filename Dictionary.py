print('Creation of a dictionary and adding values')
d={}
d=dict()
print(d)
d['MAngo']='FRUIT'
print(d)
d['MAngo']=[1,2,3]
print(d)
d['TOMATO']='VEGETABLE'
print(d)
d['TOMATO']='VEGETABLE'  # if samekey the last valuewill be ooverwritten
print(d)
d[1]='Intnum'
print(d)
d['1']='Strnum'
print(d)
d[1.2]='float'
print(d)
d[1.20]='float1'
print(d)
d[1.200000]='float1'
print(d)
d[1,2,3] = 'asas'
print(d)
d[1,2,3,4] = (1,2,3)
print(d)
d[1,2,3,4,(2,3,(2,4,5),4)] = (1,2,3)
print(d)
d[1,2,3] = 'haha'
print(d)

print("\n\nDisplay the keys in the dictionary - " , d.keys())
print("\n\nDisplay the values in the dictionary - " , d.values())
print("\n\nDisplay the items in the dictionary - " , d.items())