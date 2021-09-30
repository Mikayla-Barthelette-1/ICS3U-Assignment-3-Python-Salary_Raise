#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Sept 2021
# This program will show if a worker can earn a raise of 5%

import constants


def main():
    # this function determines if you get a raise and calculates the new salary

    # input
    salary = int(input("Please enter your salary: "))
    years_of_service = int(
        input("Please enter how many years you have worked for the company: ")
    )

    # process
    if years_of_service >= 5:
        new_salary = salary * constants.RAISE
        print("")
        print(
            "Congratulations! You got a raise of 5%. Your new salary is ${0}.".format(
                new_salary
            )
        )
    else:
        print("")
        print("You have not worked here long enough to get the raise. ")
        print("Your salary is still ${0}.".format(salary))

    # output
    print("\nDone.")


if __name__ == "__main__":
    main()
