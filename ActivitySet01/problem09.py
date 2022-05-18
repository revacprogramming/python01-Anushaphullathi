# Lists

filename = "dataset/romeo.txt"
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.strip()
    words=line.split()
    for nword in words:
        if not nword in lst:
            lst.append(nword)       
lst.sort()
print(lst)
