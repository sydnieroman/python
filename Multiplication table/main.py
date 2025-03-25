"""
This script creates a multiplication table for any value the user inputs, giving multiples of 2 up to 10.
"""

# Prompt input will be used for the "whole_num" var
whole_num = int(input("Generate a multiplication table for: "))

# Border
print("_" * 10)

# Print the user input
print(f"Number: {whole_num}")

# Print multiplication table
for i in range(2, 11, 2):
    print(f"{i}: {whole_num * i}")

# Border
print("_" * 10)


