#!/usr/bin/env python3
# Created By: Marcus Wehbi
# Date: Oct 19th, 2022
# This program displays the sum of numbers from 0 until a users number


def main():
    # declare variables
    # the final output (sum of all the numbers up until the users number)
    sum_of_numbers = 0
    # counter
    counter = 0
    # users chosen number
    user_num_string = input("Enter a whole positive number: ")
    try:
        # convert input from string to int
        user_num_int = int(user_num_string)
        # use if statement to make sure user does not input 0
        if user_num_int == 0:
            print("Enter a POSITIVE number.")
        else:
            # use while loop to calculate the sum of all the numbers
            while counter <= user_num_int:
                # add to the sum of numbers
                sum_of_numbers = sum_of_numbers + counter
                # increment by 1
                counter += 1
            # print the final sum
            print("The sum of numbers is: {}".format(sum_of_numbers))
    except:
        # statement for invalid input
        print("Please enter a valid positive whole number.")
    finally:
        # thank the user - execute no matter what
        print("Thanks for playing.")


if __name__ == "__main__":
    main()
