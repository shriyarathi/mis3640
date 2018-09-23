import math

def mysqrt(a):
    epsilon = .0001
    x = a/2

    while True:

        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y


    return y 



def test_square_root():

    print('a   mysqrt(a)     math.sqrt(a)  diff')
    print('-   ---------     ------------  ----')
    for i in range(1,10):
        print (i, mysqrt(i), math.sqrt(i), mysqrt(i)-math.sqrt(i))
    


test_square_root()