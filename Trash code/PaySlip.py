"""
eName - Employee Name
rSalary- Retainer Salary
gPay- Gross Pay
nPay- Net Pay
"""

eName= input("Please Enter Employees Name: ")
sales= float(input(f"\n{eName}, Please enter your Sales this month: " ))
rSalary= 15000.0
Commision= 0.2 * sales
gPay= rSalary + Commision
tax= 0.3 * gPay
nPay= gPay - tax

print("---------XYZ-PAYSLIP-----------")
print("\n | Employee's Name   : ", eName)
print("\n | Retainer Salary    : Ksh.15,000/=")
print("\n | Gross Pay          : Ksh.", gPay)
print("\n | Tax         : Ksh.", tax)
print("\n | Net Pay            : Ksh.", nPay)