principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate * time) / 100
print("\nSimple Interest =", simple_interest)

compound_interest = principal * (1 + rate / 100) ** time - principal
print("\nCompound Interest =", compound_interest)
