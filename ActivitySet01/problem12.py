# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
a=input("Enter the file name: ")
b=open(a)
c=re.findall(["[0-9]+",b.read()])
for i in c:
    print(sum(int(c)))