import re

#Version 1.0 - 01/18/2020, plain text - version 1.2 planned with reading a text file, processing as
#than rewriting the cleaned strings in another text file.

#Initialize text
txt = 'fdfs,"TheraininSpain",dsfddf,slfsfsld,"dfddfsg",salut,"toi"'

#sort by REGEX
x = re.findall(r"(?<=\")\w+", txt)

#Displaying x with a line break
print("\n".join(x))


