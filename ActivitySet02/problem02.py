
def add(a, b):
    sum=a+b
    return sum
    
def output(a, b, sum):
    print("sum of = ",a,b,sum)
  
def main():
    a, b = input_two_numbers()
    sum = add(a, b)
    output(a, b, sum)

if __name__ == '__main__':
  main()
