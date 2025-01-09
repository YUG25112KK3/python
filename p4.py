#W.A.P to input a number and display factorial of that number

n=int(input("enter a number:"))
facto = 1
for i in range(1,n+1):
    facto*=i
    print(f"factorial of {n} is :{facto}")
