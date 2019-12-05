x = float(input("Enter a number for x"))
y = float(input("Enter a number for y"))

if x == y:
    print("x equal y")
    if y != 0 :
        print("therfore, x / y is ", x/y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")  

print("Thanks !")              