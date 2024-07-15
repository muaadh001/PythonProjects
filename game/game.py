import random

while True:
    try:
        Level = int(input("Level: "))
    except ValueError:
        continue
    if Level <= 0:
        continue

    num = random.randint(1, Level)
    break

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess <= 0:
        continue

    if guess < num:
        print("Too small!")
    elif guess > num:
        print("Too large!")
    else:
        print("Just right!")
        break
