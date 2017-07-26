def func_check(func):   
    def wrapper(d,a):        
        if(bool(d) and bool(a)):
            return(func(d,a))
        else:
            return "Dictionaries are empty"
    return wrapper
