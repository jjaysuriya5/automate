def phonenumber():
    message = 'call me at 444-555-4242'
    pattern = re.compile( '\d{3}-\d{3}-\d{4}' )
    pat = re.search( pattern , message )
    print('Without and grouping')
    print( pat.group() )
    print('*'*25)
    
    print('Without grouping')
    message = 'call me at (444) 555-4242'
    pattern = re.compile( r'(\(\d{3}\)) (\d{3}-\d{4})' )
    pat = re.search( pattern , message )
    print( pat.group(0))
    print( 'Group - ' , pat.group(1) , '&' , pat.group(2) )
    print(pat.groups())
    print('*'*25)
    
def superhero():
    message = 'Batman and Batwomen to the rescue'
    pattern = re.compile( 'Bat(wo)?man' )
    pat =re.search( pattern , message )
    print("Super heros - " , pat.group() )
    print( re.findall( pattern , message ) )
    
def combine():
    
    text = '''Copied to clipboard:
    This project is used to extract the phone number and the email Id seperately
    (800)-420-7240
    info@nostarch.com
    media_us@nostarch.com
    415 863-9900
    705%863@9950
    222-222-2222
    academic.school@nostarch.com
    help1232@nostarch.com
    Have any interested problems lets discuss..'''
    pyperclip.copy(text)
    copied_text = pyperclip.paste()
    print('Input Text - ' , copied_text , sep = '/n')
    print()
    
    phone_pattern = re.compile(r'''(
        (\d{3}|(\d{3}\))? )        # area Code
        (\s|-|.)?                  # Seperator
        (\d{3})                    # first 3 digits
        (\s|-|.)?                  # Seperator
        (\d{4})                    # last 4 digits
    )''', re.VERBOSE )
    
    clean_text = []
    clean_text.append("Phone Numbers in given text: ")
    print( "Phone Numbers in given text: ")
    for groups in phone_pattern.findall(copied_text):
        phoneNum = re.split( '\D' , groups[0])
        print( '-'.join( [ i for i in phoneNum if i != "" ] ) )
        clean_text.append( '-'.join( [ i for i in phoneNum if i != "" ] )  )
    
    email_pattern = re.compile( '''(
    [a-zA-Z0-9._]+          # username
    @                       # @
    [a-zA-Z0-9.-]+          # domain
    (.[a-zA-Z]{2,})        # dot-something
    )''' , re.VERBOSE )
    
    print('\nEmail in given text: ')
    clean_text.append( '\nEmail in given text: ' )
    for groups in email_pattern.findall(text):
        print( groups[0] )
        clean_text.append( groups[0])
    
    
    pyperclip.copy( '\n'.join(clean_text) )
    
if __name__ == "__main__":
    import re
    import keyboard 
#     phonenumber()
#     print('-'*100)
#     superhero()
#     print('-'*100)
    combine()
    print("\nPress ctrl+v you will get the extracted text..")
    keyboard.press_and_release('ctrl + v')