def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
    
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
    
def sum_series(n, param1, param2):
    if param1 == 0 and param2 == 1:
        return fibonnaci(n)
    elif param1 == 2 and param2 == 1:
        return lucas(n)
    else:
        return sum_series(n-1) + sum_series(n-2)