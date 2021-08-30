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
            a = float(input('#1 -- '))
            b = float(input('#2 -- '))
    
            print('--------- + ')
            print(a + b)

    if(x) == '2' :
            c = float(input('#1 -- '))
            d = float(input('#2 -- '))
    
            print('--------- - ')
            print(c - d)

    if(x) == '3' :
            e = float(input('#1 -- '))
            f = float(input('#2 -- '))
    
            print('---------- *')
            print(e * f)

    if(x) == '4' :
            g = float(input('#1 -- '))
            h = float(input('#2 -- '))
    
            print('----------- /')
            print(g / h)


