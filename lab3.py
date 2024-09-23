salary = int(input("Enter your salary: "))

loan = int(input("Enter loan amount: "))

if (salary >= int(30000) and loan < salary*10):
    print("You are eligible for the loan")
elif salary<int(30000) or loan>salary*10:
    print("You are not eligible for this loan")

if salary<30000: 
    print("Reason: Salary too low"),exit()
    pass
if loan>salary*10:
    print("Reason: Loan too high"),exit()
    pass

month = int(input("Months to pay: "))
print("Loan with interest:", (loan*1.10))