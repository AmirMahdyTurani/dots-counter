# In the name of Allah

"""
A program that caculate a persian text dots.
v 1.3.1
"""

# Grouping letters
one_dots = ["ض", "ف", "غ", "خ", "ج", "ب", "ن", "ظ", "ز", "ذ"]
two_dots = ["ق", "ت"]
three_dots = ["ث", "چ", "ش", "پ"]
middle_dots = ["ی"]

# dots counter
dots = 0

# user text
text = input("Please Enter your text: ")

# calculate dots with for loop and itreate on user's text letters
for char in text:
    if char in one_dots:
        dots += 1
    elif char in two_dots:
        dots += 2
    elif char in three_dots:
        dots += 3
     #handling the "ی" character that if it is in the last of text doesn't have any dot but in the first and middle of text has two dot
    elif char in middle_dots and text.index(char) != (len(text) - 1):
        dots += 2
     # for another characters
    else:
        continue

# show result to user
print(dots)
