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
getting error
'''
a=int(input())
for i in range(a):
  n=int(input())
  for j in range(n):
    if j[0]>j[1]:
      print(j[0])
    else:
      print(j[1])
      
  

