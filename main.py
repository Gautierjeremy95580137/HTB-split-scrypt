import re

#Version 1.2 - 28/02/2021.

#reading file txt

file = open("test.txt", "r")

#regex on file
x = re.findall(r"(?<=\")\w+[\w\-\?\-\/\.\=\&\;\$\:\+\!\%\@]*", file.read())
file.close()

#carriage return
y = "\n".join(x)

#create a new file and write
fichier = open("data.txt", "a")
fichier.write(y)
fichier.close()






