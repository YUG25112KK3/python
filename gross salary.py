"write a program to enter employee ID ,EMPLOYEE NAME AND BASIC SALARY FROM USER CALCULATE HRA 10%,DA 8%,TA 11%,PF 12%,FIND OUT GROSS SALARY FORMULA IS (BS+HRA+DA+TA-PF) IF GROSS SALARY"


empId=int(input("Enter the EMP ID:"))
empName=input("Enter the EMP Name:")
basicSal=int(input("Enter the basic salary:"))
hra=(basicSal*0.10)
da=(basicSal*0.08)
ta=(basicSal*0.11)
pf=(basicSal*0.12)

grossSal=(basicSal+hra+da+ta-pf)

print(f"Emp ID: {empId}")
print(f"Emp Name: {empName}")
print(f"Basic Salary: {basicSal}")
print(f"HRA (10%): {hra}")
print(f"DA (8%): {da}")
print(f"TA (11%): {ta}")
print(f"PF (12%): {pf}")
print(f"Gross Salary: {grossSal}")
