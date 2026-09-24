#!/usr/bin/env python3
# Created By: Kaylee Ralejoe
# Date: 15,09,2026
# This program asks for length and width
# of a rectangle, calculates and displays the area and perimeter
# back to the user in proper units.


def main():
    # get the length from the user and convert it into an interger
    length = int(input("Enter length of the rectangle (cm): "))

    # get the width from the user and convert it into an interger
    width = int(input("Enter width of the rectangle (cm): "))

    area = length * width
    perimeter = 2 * (length + width)

    # display the area and perimeter to the user in proper units
    print("The area is: {}cm²".format(area))
    print("The perimeter is: {}cm".format(perimeter))


if __name__ == "__main__":
    main()
