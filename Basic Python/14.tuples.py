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


#This is about tuples in python
#A tuple is an ordered collection of values.
# A tuple is immutable and cannot be changed after creation.
# A tuple is defined using parentheses.
# The elements in a tuple can be accessed using their index.
# The syntax for accessing the elements of a tuple is as follows:

# Create a tuple
fruits = ("apple", "banana", "cherry")

# Access elements by index
first_fruit = fruits[0]
second_fruit = fruits[1]

# Iterate over the tuple
for fruit in fruits:
    print(fruit)

# Tuple with mixed data types
person = ("John", 30, "New York")

# Unpacking a tuple
name, age, city = person

# Nested tuples
nested_tuple = (1, ("a", "b"), 2)

# Tuple with a single element (need a comma at the end)
single_element_tuple = (42,)

# Tuple methods
num = fruits.count("apple")  # Count the number of occurrences of "apple"
index = fruits.index("banana")  # Get the index of "banana"

# Length of a tuple
length = len(fruits)

print("First fruit:", first_fruit)  # Output: First fruit: apple
print("Second fruit:", second_fruit)  # Output: Second fruit: banana
print("Person:", name, age, city)  # Output: Person: John 30 New York
