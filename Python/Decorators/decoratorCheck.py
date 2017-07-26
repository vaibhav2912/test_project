from decorator import func_check

d={'one':1}
a={'two':2}

@func_check
def func(d,a):
    return d,a
    
    
    
print(func(d,a))