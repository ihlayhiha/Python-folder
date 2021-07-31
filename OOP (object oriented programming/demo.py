a_string = "This is a \nstring split and \n\t\tthis is tabbed twice"
print(a_string)

raw_string = r"This is a \nstring split and \n\t\tthis is a tabbed  twice"
print(raw_string)

another = """Does this also \nsplit the string?"""
print(another)

raw_string = r"""This does not \nsplit the string"""
print(raw_string)

b_string =  "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "this is double tabbed"
print(b_string)

backslash_string = "this is a backslash \followed by some text"
print(backslash_string)

backslash_string = "this is a backslash \\followed by some text"
print(backslash_string)

error_string = r"this string ends with \\"
print(error_string)