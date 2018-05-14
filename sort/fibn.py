import numpy as np

def fib(n): 
    if n<2 :  
       return n
    else : 
       return (fib(n-1) + fib(n-2))

def dynamic_fib(n):
    f = 1
    g = 0
    while n > 0:
        g = g + f
        f = g - f
        n = n - 1
    return g


if __name__ == '__main__':
    for i in range(40):

        print('fib_dyn',i,dynamic_fib(i))

        print('fib',i,fib(i))
