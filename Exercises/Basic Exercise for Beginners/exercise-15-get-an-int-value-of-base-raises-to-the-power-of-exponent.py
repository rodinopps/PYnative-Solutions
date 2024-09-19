def exponent(base, exp):
    return f"{base} raises to the power of {exp}: {base ** exp}"

base = int(input("Enter a base: "))
exp = int(input("Enter an exponent: "))
print(exponent(base, exp))
