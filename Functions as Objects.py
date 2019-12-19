def applyToEach(l, f):
    """assumes l is a list, f a function
       mutates l by replacing each element,
       e, of l by f(e)""" 
    for i in range(len(l)):
           l[i] = f(l[i]) 

l = [1, -2, 3.4]    

applyToEach(l, abs)
print(l)
applyToEach(l, int)
print(l)
applyToEach(l, fib)
print(l)

