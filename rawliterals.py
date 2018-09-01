
# =====================================
# Demo of raw literals and others
# =====================================

# =========================================
# using \ to represent special characters
# =========================================

# Here we are adding \ with \n  for (newline) and \t for (tab)

print("="*40)
a_string = "This is \na string split \t\tand tabbed"
print(a_string)
print("="*40)

# ==================
# rawstring using r
# ==================

# if we want to write this line ("This is \na string split \t\tand tabbed") as it is,
# we use "r" in front of it to represent rawstring, hence it overides the special characters \n and \t

r_string = r"This is \na string split \t\tand tabbed"
print(r_string)
print("="*40)

# =======================
# rawstring using chr(i)
# =======================

# Another way to print rawstrings is by using chr(x) where i is an integer
# https://docs.python.org/2/library/functions.html#chr

# chr(i) - Return a string of one character whose ASCII code is the integer i.
#          For example, chr(97) returns the string 'a'. This is the inverse of ord().
#          The argument must be in the range [0..255], inclusive;
#          ValueError will be raised if i is outside that range. See also unichr().

# Here is an example of writing rawstring using chr(i)

b_string = "This is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)
print("="*40)

# Here are other representations from chr(i)

print(chr(1))
print(chr(97))
print(chr(98))
print(chr(99))
print(chr(8364))
print("="*40)

# ================================
# using double \\ to represent \
# ================================

# if you want to represent backslash (\), you will need to use two backslash
# for example, in this first code, we used one \ next to f and f did not show up because \f is a representation of an upward arrow

backslash_string = "This is a backslash \followed by text"
print(backslash_string)

# To print backslash, we need to have two backslashes

backslash_string = "This is a backslash \\followed by text"
print(backslash_string)
print("="*40)

# NOTE that if you want to represent a backslash at the end of the line, it needs to be double.
# if you use single backslash at end of string e.g. "string \", it will create error message because \" is a special character,
# hence string will not be closed by "
# you will need double \\ as shown for normal string and raw literal string (starting with r")

error_string = "This string ends with \\"  # Normal string
print(error_string)
error_string = r"This string ends with \\"  # Raw literal string
print(error_string)



