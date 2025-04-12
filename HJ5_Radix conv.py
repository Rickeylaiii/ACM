s = input().strip()
"""
Hexadecimal to Decimal Converter

This script reads a hexadecimal string from standard input and converts it to a decimal integer.

Input:
    A string representing a hexadecimal number (can include 0x prefix, though not required)

Output:
    The decimal (base 10) equivalent of the input, printed to standard output

Example:
    Input: "1A"
    Output: 26

Note:
    - Input is automatically stripped of leading/trailing whitespace
    - Both uppercase and lowercase hexadecimal digits (A-F/a-f) are accepted
    - This is a solution for HJ5 which requires conversion between number systems
"""
x = int(s, 16)
print(x)