x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print("low = " + str(low) + " high " + str(high) + " ans = " + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0      
print("numGuesses = " + str(numGuesses))    
print(str(ans) + " is close to square root of " + str(x))  
#####################################################################

cube = 27
epsilon = 0.01
numGuesses = 0
low = 0
high = cube
guess = (high + low) /2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube :
        low = guess
    else:
        high = guess 
    guess = (high + low)/2.0
    numGuesses += 1   
print("numGuesses =", numGuesses)
print(guess, "is close to the cube root of", cube)
