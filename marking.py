#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Oct 2021
# This program uses a list to find the average mark


def average_numb(list_numb):
    # This program uses a list to find the average mark

    total = 0
    total_number = 0
    count = 0
    for count in range(0, len(list_numb)):
        total += list_numb[count]
        total_number += 1

    average = total / total_number

    average = average * (10 ** 2) + 0.5
    average = int(average)
    average = float(average)
    average = average / (10 ** 2)

    return average


def main():
    # This program uses a list to find the average mark

    words = []
    temp_w = None

    # input
    print("Please enter 1 mark at a time. Enter -1 to end.")
    print("")

    temp_str = input("What is your mark (as %): ")
    try:
        temp_w = int(temp_str)
        words.append(temp_w)

        while temp_str.upper() != "-1":
            temp_str = input("What is your mark (as %): ")

            try:
                temp_w = int(temp_str)
                words.append(temp_w)

            except Exception:
                print("These are invaild numbers.")
                print("")
        words.pop()

        average = average_numb(words)
        print("")
        print("The average is {0}%".format(average))

    except Exception:
        print("")
        print("These are invalid numbers.")
        print("")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
