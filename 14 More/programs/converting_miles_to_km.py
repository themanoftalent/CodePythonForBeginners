##################################################
#### **************************************** ####
#### !/usr/bin/python3                        ####
#### -*- coding: utf-8 -*-                    ####
#### @Time    : 2023/20/10 11:40              ####
#### @Author  : themanoftalent                ####
#### @Site:https://github.com/themanoftalent  ####
#### @Project : python-app                    ####
#### **************************************** ####
##################################################

# Function to convert miles to kilometers
def miles_to_km():
    # Input from the user
    miles = float(input("Enter a distance in miles: "))
    conv_fac = 1.609  # Conversion factor from miles to kilometers

    # Calculating distance in kilometers
    kilometers = miles * conv_fac

    # Display the result
    print("The distance in kilometers is: ", kilometers)


# Call the function
miles_to_km()
