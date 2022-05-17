fname=input("Enter the file name: ")
fhand=open(fname)
count=0
if line in fhand:
  if line.startswith("Subject:"):
      count=count+1
  print("The no. of words are ",count,"In file ",fname)
  python ActivitySet01/extra.py




