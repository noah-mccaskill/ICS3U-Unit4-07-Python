#!/usr/bin/env python3

# Created by Noah McCaskill
# Created May 2022
# This program shows values from 1000 - 2000


def main():
    # this function shows values from 1000 - 2000
    # with a new line every 5 numbers

    # process, output
    for counter in range(1000, 2000 + 1):
        if counter % 5 == 0:
            print("\n{0}".format(counter), end=" ")
        else:
            print("{0}".format(counter), end=" ")

    print("")
    print("\nDone.")


if __name__ == "__main__":
    main()