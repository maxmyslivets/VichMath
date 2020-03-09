from numpy import array, dot, linalg


def result(ur, ur1):
    
    """разбивка уравнений на их элементы"""
    """c = ur.split('=')[1]
    c1 = ur1.split('=')[1]
    a = ur[:ur.index('x')]
    a1 = ur1[:ur1.index('x')]
    b = ur[ur.index('x')+1:ur.index('y')]
    b1 = ur1[ur1.index('x')+1:ur1.index('y')]"""

    c = float(ur.split('=')[1])
    c1 = float(ur1.split('=')[1])
    a = float(ur[:ur.index('x')])
    a1 = float(ur1[:ur1.index('x')])
    b = float(ur[ur.index('x')+1:ur.index('y')])
    b1 = float(ur1[ur1.index('x')+1:ur1.index('y')])


    def el_1(a, a1, b, b1, c, c1):
        """Первый эелемент матрицы"""
        
        x = ((1*c)+((-b/b1)*c1)) / ((1*a)+((-b/b1)*a1))
        y = ((-a1/a)*c+1*c1)/((-a1/a)*b+1*b1)

        """print(
            'Первый элемент матрицы:\n',
            '(1*'+str(c)+'+('+str(-b)+'/'+str(b1)+')*'+str(c1)+'))',
            '/',
            '(1*'+str(a)+'+('+str(-b)+'/'+str(b1)+')*'+str(a1)+'))',
            '=', x
        )
        print(
            'Второй элемент матрицы:\n',
            '('+str(-a1)+'/'+str(a)+')*'+str(c)+'+1*'+str(c1)+'))',
            '/',
            '('+str(-a1)+'/'+str(a)+')*'+str(b)+'+1*'+str(b1)+'))',
            '=', y
        )"""

        return [x, y]
    
    #el_1(a, a1, b, b1, c, c1)

    return [a, a1, b, b1, c, c1]


"""ur = '2x+1y=7'
ur1 = '1x+3y=11'"""

# result(ur, ur1)