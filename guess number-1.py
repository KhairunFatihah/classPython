#!/usr/bin/env python

import random


def main():
    """Start a number guessing game between 1 - 100."""
    print("guess the number!")

   # X = random.gammavariate(1, 100)
     x = random.betavariate(1, 2)
    print(X)
    guess = None

    while X != guess:

        guess = int(input("Pick a number between 1 to 100: "))

        if X == guess:
            print("You genius!")
            break
        else:
            print("lol. lmao")
           
main()
