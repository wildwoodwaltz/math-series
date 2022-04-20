
def fibonacci(n):
    '''
    The Fibonacci sequence is a list of numbers starting with zero where the first value is added to the second value to create a third value. 
    This occours recursively to infinity. This function will return the fibbonacci number at position given any int input for n 
    '''
    if n<=1:
        return n
    else:
        return(fibonacci(n-1)+ fibonacci(n-2))

def lucas(n):
    '''
    Much like the fibonacci sequence where first value is added to second value to return a third value.
    Lucas sequence instead starts with [2, 1] instead of [0,1] that the fibonacci sequence does.
    This function will return any numbe in the lucas sequence at n. 
    '''
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return(lucas(n-1)+ lucas(n-2))