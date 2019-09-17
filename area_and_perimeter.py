#!/user/bin/env python3

# Created by: Jaeyoon
# Created on: Sept 2019
# This program calculates the area and perimeter of rectangle
#     with user input


def main():
    # this function calculates area and perimeter
    
    # input
    length = int(input("Enter length of the rectangle (mm): "))
    width = int(input("Enter width of the rectangle (mm): "))
    
    # process
    area = length*width
    perimeter = 2*(length+width)
    
    # output
    print("")
    print("Area is {}mm^2".format(area))
    print("Perimeter is {}mm".format(perimeter))
    
    
if __name__ == "__main__":
    main()
