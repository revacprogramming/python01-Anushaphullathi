'''input format
4
2 5
5 7
6 6
7 3

   output format
5
7
same,6
7
very important for taking many input in one line
use 
x,y=map(int,input().split())
if you know the no. of stuff

but if it is many make it a list
l=list(map(int,input().split()))

now try
'''
a=int(input())
for i in range(a):
  x,y=map(int,input().split())
  if(x==y):
    print("same"+","+str(x))
  else:
    print(max(x,y))
  
'''
5
2 5
6 6
7 9 
6 5 
4 3

output
avg
'''
a=int(input())
for i in range(a):
  l=list(map(int(a),input()))
  print(sum(l)/len(l))

a=int(input())
for i in range(a):
  l=list(map(int(a),input().split()))
  s=sum(l)/len(l)
if(s>0):
  print("YES")
else:
  print("NO")
  
  


      
  

