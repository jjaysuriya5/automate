print('Basic String Functions....')
s1='Hello world'
print( "Lower case - " ,  s1.lower() )
print("Find Index positions..")
print('o - ' , s1.find('o'))
print('h - ' , s1.find('h'))
print('1 - ' , s1.find('1'))
print('or from 7 to 9 ' , s1.find('or',7,9))

print('Starts with H - ' , s1.startswith('H'))

print('Count occurance of l -' , s1.count('l'))

print('Repalce all l to L - ' , s1.replace('l','L'))
print('Repalce 1st occurance of l to L - ' , s1.replace('l','L', 1))

print('Strip H from the string - ', s1.strip('H')) 

print("Some Sample Examples....")
print('\n')
print( 'Write a program to identify the palindrome word in a line of text ')
ip_str = input("Enter the String : ")
ip_lst = ip_str.split()
# print(ip_lst)
op_lst=[]
for i in ip_lst:
    if ( i.lower() == i[::-1].lower()):
        op_lst.append(i)
# print(op_lst)
print("The palindrome workds in the string are : ")
for j in op_lst:
    print(j)
print()
print('Write a program to remove the character at odd index')    
ip_str = input("Enter a string : ")
op_str = ip_str[::2]
print( "The characters at even index is " ,op_str )