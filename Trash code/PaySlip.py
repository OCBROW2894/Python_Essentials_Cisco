"""
Question(Problem) - Company XYZ LTD, A fast moving good selling Company Pays it's Employees on a retainer Salary of Ksh. 15,000
                    Plus the Commision of 20% of Sales. The Employees are subjected to a 30% tax on Gross Pay
                    
                    Additional Information
                    Gross Pay = Retainer salary Plus Commision
                    Net Pay= Gross Pay Minus Tax
                    
eName - Employee Name
rSalary- Retainer Salary
gPay- Gross Pay
nPay- Net Pay

Updates- Changed the Commision Calculations from the general 20% of sales
        To a Different commision based on amount of sales
"""

eName= input("Please Enter Employees Name: ")
sales= float(input(f"\n{eName}, Please enter your Sales this month: " ))
rSalary= 15000.0
#Commision= 0.2 * sales  #Old Commission Formula
if sales>=1000000:
    Commision = sales * 0.25
elif sales>= 500000:
    Commision = sales * 0.20
elif sales>= 250000:
    Commision = sales * 0.1
elif sales>= 100000:
    Commision = sales * 0.05
else:
    Commision = 0
    
gPay= rSalary + Commision
tax= 0.3 * gPay
nPay= gPay - tax

print("---------XYZ-PAYSLIP-----------")
print("\n | Employee's Name   : ", eName)
print("\n | Retainer Salary    : Ksh.15,000/=")
print("\n | Gross Pay          : Ksh.", gPay)
print("\n | Commission          : Ksh.", Commision)
print("\n | Tax         : Ksh.", tax)
print("\n | Net Pay            : Ksh.", nPay)