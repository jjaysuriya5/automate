import os
path = os.getcwd()
print('Current Path - ' , path )

print('\nAutomatically getting the path for dummy files [ \'a.txt\' , \'b.txt\' , \'c.txt\' ] : \n')
for file in [ 'a.txt' , 'b.txt' , 'c.txt' ]:
    print( os.path.join(path , file ) )

print('\nPrint the absolute path - ' , os.path.abspath('.'))
print('\nCheck the absolute path - ' , os.path.isabs('.'))
print('\nPrint the absolute path - ' , os.path.isabs( os.path.abspath('.')) )

print('\nRelative path - ' , os.path.relpath('C:\\windows' , 'C:\\') )
print('\nRelative path - ' , os.path.relpath('C:\\windows' ) )
print('\nRelative path - ' , os.path.relpath('C:\\windows' , 'C:\\s\\d') )

print('\nCurrent Path - ' , path )
print('\nBase name of current path : ' , os.path.basename(path) )
print('\nDirectory name of name of current path : ' , os.path.dirname(path) )
print('\nBase name + directory name : ' , os.path.split( path ) )
print('\npath seperator - ' , os.path.sep)
print('*'*100)

filename = 'dummy.txt'
print('\nCreating new file and adding a line')
with open( filename , 'w') as f:
    f.write('Empty File added..\nSecond Line')

print('\nDisplaying the content of the file')
with open(filename , 'r') as f:
    print( f.read() )
    
with open(filename , 'r') as f:
    print( f.readlines() )
    
with open(filename , 'r') as f:
    for line in f:
        print(line.strip('\n'))
print('*'*100)    

print('\nAbsolute path of the file : ' , os.path.abspath(filename)  )
print('\nGetting the size of the file - ' , os.path.getsize( os.path.abspath(filename) ) , 'bytes')

print('\nChecking if the path exist - ' , os.path.exists('C:\\d'))
print('\nChecking if the path exist - ' , os.path.exists(os.path.abspath('.')))
print('\nChecking if the path exist - ' , os.path.exists(os.path.relpath( os.path.abspath('.') ) ) )