cube = 27
epsilon = 0.01
numGuesses = 0
low = 0
high = cube
guess = (high + low) /2.0
if cube > 0:
    while abs(guess**3 - cube) >= epsilon:
        if guess**3 < cube :
            low = guess
        else:
            high = guess 
        guess = (high + low)/2.0
        numGuesses += 1   
    print("numGuesses =", numGuesses)
    print(guess, "is close to the cube root of", cube)
else:
    while abs(guess**3 - cube) >= epsilon:
        if guess**3 < cube :
            high = guess
        else:
            low = guess 
        guess = (high + low)/2.0
        numGuesses += 1   
    print("numGuesses =", numGuesses)
    print(guess, "is close to the cube root of", cube)

