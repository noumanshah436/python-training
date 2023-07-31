import random


def guessGame(a, b, actual):
    guess = int(input(f"Guess a number between {a} and {b} : "))
    nguess = 1
    while guess != actual:
        if guess < actual:
            guess = int(input(f"Enter a bigger number : "))
            nguess += 1
        else:
            guess = int(input(f"Enter a smaller number : "))
            nguess += 1

    print(f"You guessed the number in {nguess} guesses ")
    return nguess


if __name__ == "__main__":
    a = int(input("Enter 1st Number : "))
    b = int(input("Enter 2nd Number : "))
    actual1 = random.randint(a, b)
    print("\nPlayer 1's turn")
    g1 = guessGame(a, b, actual1)
    print("\nPlayer 2's turn")
    actual2 = random.randint(a, b)
    g2 = guessGame(a, b, actual2)

    if g1 < g2:
        print("\nPlayer 1 won the match!\n")

    elif g1 > g2:
        print("\nPlayer 2 won the match!\n")

    else:
        print("\nIts a Tie!\n")

    print(f"Player 1 actual guess : {actual1}")
    print(f"Player 2 actual guess : {actual2}")

    input("continue ...")