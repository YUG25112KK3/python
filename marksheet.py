s1=int(input("enter marks:"))
s2=int(input("enter marks:"))
s3=int(input("enter marks:"))
s4=int(input("enter marks:"))

total=s1+s2+s3+s4
pr=total/4

print(total)
print(pr)
if s1>=40 and s2>=40 and s3>=40 and s4>=40:
    print("Result:Pass")
if pr>=70:
    print("grade is:A")
elif pr>=60 and pr<70:
    print("grade is:B")
elif pr>=50 and pr<60:
    print("grade is:C")
elif pr>=40 and pr<50:
    print("grade is:D")
else:
    print("Result:Fail")
