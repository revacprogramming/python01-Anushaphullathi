# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
a=input("Enter the file name: ")
b=open(a)
c=re.findall(["[0-9]+",b.read()])
for i in c:
    print(sum(int(c)))

#short form
#import re
#print(sum([int(i) for i in re.findall("[0-9]+",open(name).read())]))