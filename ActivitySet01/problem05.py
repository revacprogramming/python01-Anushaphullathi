# Functions
def computepay(h,r) :
    if h < 40 :
        p= h*r
    elif h > 40 :
        p= 40*r + (h-40)*1.5*r
    return p

hrs = input("Enter hours : ")
h = float(hrs)
rt = input("Enter the rate : ")
r = float(rt)
p = computepay(h,r)
print("Pay",p)
