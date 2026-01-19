import random

while True:
    Turn = input("move your turn y/n :   ").lower()
    if Turn == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"({die1},{die2})")
    elif Turn == 'n':
        print("thanks for playing")
        break
    
    else:
        print("invalid Turn")