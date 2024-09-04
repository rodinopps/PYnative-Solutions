income = int(input("Enter income: "))
if income <= 10000:
    print("Total tax to pay is 0")
elif income <= 20000:
    print("Total tax to pay is", income * 0.10)
elif income > 20000:
    print("Total tax to pay is", 10000 * 0.10 + (income - 20000) * 0.2)
