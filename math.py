#add unit convertor 
print('Turn on calculator?')
if input('y or n -- ') == 'y':
    print('''
- - - - - - Menu - - - - - -
    1 - addition
    2 - subtraction
    3 - multiplication
    4 - division''')
    
    x = input()

    if(x) == '1' :
            a = int(input('#1 -- '))
            b = int(input('#2 -- '))
    
            print('--------- + ')
            print(a + b)

    if(x) == '2' :
            c = int(input('#1 -- '))
            d = int(input('#2 -- '))
    
            print('--------- - ')
            print(c - d)

    if(x) == '3' :
            e = int(input('#1 -- '))
            f = int(input('#2 -- '))
    
            print('---------- *')
            print(e * f)

    if(x) == '4' :
            g = int(input('#1 -- '))
            h = int(input('#2 -- '))
    
            print('----------- /')
            print(g / h)


