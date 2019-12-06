x = int (input ("Enter an integar: "))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + " is not a perfect cube") 
else:
    print("cube root of " + str(x) + " is " + str(ans))    

###################################################################    

x = int (input ("Enter an integar: "))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(str(x) + " is not a perfect cube") 
else:
    if x < 0:
        ans = - ans
    print("cube root of " + str(x) + " is " + str(ans))    

###################################################################    

cube = 27
for Guess in range(cube+1):
    if Guess**3 == cube:
        print("cube root of", cube, "is", Guess)

###################################################################

cube = -27
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, "is not a perfect cube")
else:
    if cube < 0:
        guess = - guess
    print("Cube root of " + str(cube) + " is " + str(guess))    


