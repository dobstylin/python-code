"""This function will ask for numbers 1 at a time and then find the gcd to determine coprime"""
def coprime_test_loop():
    while True:
        a = int(input('Enter the first number: '))
        b = int(input('Enter the second number: '))
        (coprime(a,b))
        if (coprime(a,b)) == True:
            print(a, 'and', b, 'are coprime')
            """The character q will quit the function, any other function will continue the loop"""
            y = input('Enter q to quit, any other character to continue')
            if y == 'q':
                break
            else:
                coprime_test_loop()
        else:
            print(a, 'and', b, 'are not coprime')
            """The character q will quit the function, any other function will continue the loop"""
            y = input('Enter q to quit any other character to continue')
            if y == 'q':
                break
            else:
                coprime_test_loop()
            
def coprime(a,b):
    import math
    x = math.gcd(a,b)
    if x == 1:
        return True
    else:
        return False
      
