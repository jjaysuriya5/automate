print('creation of lists..')

l1=[]
l2=list() 

print((l1))
print((l2))

print('\n\nAssigning and Indexing..')

# assiging value for list

l1=[1,0,3,4,5]
l2=[1.2,0.2,2,3,4,5]
l3=[1,0,3,4,5,'1','AWA','1w1']
l4=[1,0,3,4,5,[1,'1asa',['aas','asa',['asaas']]]]

print('Orginal List - ' , l4)
print(l4[1])
print(l4[5])
print(l4[5][1]) # accessing elemente inside list of list
print(l4[5][1][1])  # accessing elemente inside list of list
print(l4[5][2][0][2])

print("\n\nList Slicing")
l1=['a','aa','aaa','asdf']
print(l1[0:2])
print(l1[0:2][0])
print(l1[0:1])
print(l1[0:1][0])
print(l1[0:1][-1])
print(l1[5:6]) # no eror as this is just displaying , accessing throws error
# print(l1[5])

print('\n\nOther Functions')
l=[1 , 5 , 2 , 8 , 7 , 0 ]
print('Orginal List - ' , l )

print( 'Sorted list (ascending) - ' , sorted( l , reverse = False ) )
print( 'Sorted list (descending) - ' , sorted( l , reverse = True ) )

print('poping element')
l.pop()
print(l)
l.pop()
print(l)

print('\n\nLambda operations using list')
ls=[1,2,3,4,5,6,7]
print('Orginal List - ' , ls)

print('Multiply all elements in list by 2')
f_l = list(map ( ( lambda x:x*2) , ls ) )
print(f_l)

print('Filter out only even numbers')
f_l = list(filter ( ( lambda x:x%2 == 0) , ls ) )
print(f_l)

from functools import reduce
print('Sum of elements using lambda')
total = reduce ( lambda x,y : x+y, ls  )
print(total)