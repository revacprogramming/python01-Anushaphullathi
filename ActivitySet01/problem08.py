# Files
filename = "dataset/mbox-short.txt"
name=input("Enter the file name: ")
fhand=open(name)
xfile=fhand.read()
for line in xfile:
    l=xfile.rstrip()
    if not l.startswith("X-DSPAM-Confidence:    0.8475"):
        continue
    else:
        count=0
        starting_point=0
        count=count+1
        staring_point=l.find("0")
        floating_point=float(l[starting_point:])
        total=starting_point+floating_point
average=total/count
print("Average spam confidence: ",average)
      
        
       
    
      




