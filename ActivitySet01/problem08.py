# Files
# Use the file name mbox-short.txt as the file name
#filename = "dataset/mbox-short.txt"
name=input("Enter the file name: ")
fhand=open(name)
total=0
count=0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x=line.find("0")
    y=float(line[x:])
    count=count+1
    total=total+y
    
average=total/count
print("Average spam confidence:",average)
      
        
       
    
      




