#add unit convertor 
print('Turn on calculator?')
if input('y or n -- ') == 'y':
    print('''
- - - - - - Menu - - - - - -
    1 - addition
    2 - subtraction
    3 - multiplication
    4 - division
    5 - Conversion''')
    
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

    if(x) == '5' :
        print('''
- - - - - - Menu - - - - - -
        1 - INCHES TO CM
        2 - Miles
        3 - no dont click me
            ''')
        y = input()

        if(y) == '1':
                print('''- - - Menu - - -
                        1 - in to cm
                        2 - cm to in
                        ''')
                z = input()
                
                if(z) == '1':
                                        a = float(input('in -- '))
                                        print(a * 2.54)

                if(z) == '2':
                                        a = float(input('cm -- '))
                                        print(a / 2.54)

        if(y) == '3':
                                print('yo mama')
