import math

r=int(input('Enter the Radius of the Circle :'))
a=math.pi*pow(r,2)
print('The area of Circle is :' , a )

# print('Program to get the area  of the Triangle :')
print('------------------------------------------')
b=int(input('Enter the base of the triangle : '))
h=int(input('Enter the height of the triangle : '))
a=0.5*b*h
print('Base is : ', b , ' Height is : ' , 'Area is : ' , a)

tempc1=float(input("Enter the Temperature in Celcius :"))
tempf1=((9/5)*tempc1)+32
print("The temperature in Fahrenheit is : " ,tempf1 )

def fibbo(n):
    if n<=1:
        return n
    else:
        return fibbo(n-1)+fibbo(n-2)

No_of_terms = int(input("Enter the number of terms for fibonnaci series : "))
for i in range(No_of_terms):
    print(fibbo(i))
