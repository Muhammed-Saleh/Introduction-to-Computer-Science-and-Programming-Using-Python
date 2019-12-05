x = int (input("Enter an integer: "))
y = int (input("Enter an integer: "))
z = int (input("Enter an integer: "))

if x < y and y < z:
    print("x is least")
elif y < z:
    print("y is least")
else:
    print("z is least")    
