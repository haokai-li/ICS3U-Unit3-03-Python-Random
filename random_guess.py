#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Sept 2021
# This Program guess a number between 0 - 9 (random)

import random


def main():
    # This function guess a number between 0 - 9 (random)
    answer = random.randint(0, 9)

    # input
    number = int(input("Enter a number between 0 - 9: "))
    print("")

    # process
    if number == answer:
        # output
        print("You guessed correctly!")
    else:
        # output
        print("You guessed wrong!")

    print("")
    print("Answer: {}".format(answer))
    print("\nDone")


if __name__ == "__main__":
    main()
