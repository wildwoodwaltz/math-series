
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

def sum_series(n, x=0, y=1):
    '''
    Sum Series takes three arguments
    First argument n is the position in the series you'd like to know.
    Second argument is x which represents first number in the series.
    Third argument is y which represents the second number in the series.
    Then it returns the number at the position n if each number was added to the previous number given two starting numbers
    If no x or y is givin it will return the fibonacci sequence.
    '''
    if n == 1:
        return x
    elif n == 2:
        return y
    else:
        return(sum_series(n-1)+ sum_series(n-2))