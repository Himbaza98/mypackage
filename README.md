# mypackage

# Overview
This Python package provides a simple function to retrieve the top N numbers in descending order from a given list of items. It is designed to be a convenient utility for scenarios where you need to quickly identify and extract the highest values from a dataset.

# Installation
To install the package, you can use the following command:

pip install topn-numbers

# usage

from topn_numbers import get_top_n_numbers

# Example usage:
numbers_list = [23, 56, 12, 89, 45, 67, 34, 78]
n_value = 3

result = get_top_n_numbers(numbers_list, n_value)
print(f"Top {n_value} numbers in descending order: {result}")

Replace numbers_list with your own list of numerical values and n_value with the desired number of top elements.

# Function Documentation
get_top_n_numbers(numbers, n)

# Parameters:

numbers (list): List of numerical values.
n (int): Number of top elements to retrieve.

# Returns:

list: List containing the top N numbers in descending order.

# Example
Given the example usage above:

numbers_list = [23, 56, 12, 89, 45, 67, 34, 78]
n_value = 3

result = get_top_n_numbers(numbers_list, n_value)
print(f"Top {n_value} numbers in descending order: {result}")

# output
Top 3 numbers in descending order: [89, 78, 67]

# License
This package is licensed under the MIT License - see the LICENSE file for details.