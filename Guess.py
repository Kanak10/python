n = 63

while True:
    g = int(input("Guess a number : "))

    if g == n:
        print("you win the Game")
        break
    
    elif n < g:
        print("Guess Small Number")

    elif n > g:
        print("Guess Large Number")