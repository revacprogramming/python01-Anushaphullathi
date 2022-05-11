# Conditional Execution
hrs=input("Enter hours ")
h=float(hrs)
rp=input("Enter rate per hour ")
x=float(rp)
if float(hrs)<40:
	print(h*x)
elif float(hrs)>40:
	print(40* x + (h-40)*1.5*x)

