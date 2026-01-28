def factorial(n):
    if n==0 or n==1:
        return 1
    elif n<0:
        return "factorial not defined for negative numbers"
    else:
        return n*factorial(n-1)
    
n=int(input("enter number:"))
print("factorial of",n,"is",factorial(n))

    