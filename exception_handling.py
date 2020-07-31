# example of normal exception handling

a = int(input("Enter a number A : "))
while True :
    b = int(input("Enter a number B : "))
    try :
        d = a / b
        break
    except :
        print("Division of zero is not possible...Enter a non zero number...")
print("Division is" , d )

print('\n\nOpening a file which doesnot exist')
try :
    fh = open('open.txt' , 'r')
    print("file opened successfully")
    for i in fh:
        print(i , end ='')
    
except :
    print("File cannot be opened")

finally :
    fh.close()
