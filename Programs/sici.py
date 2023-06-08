p=float(input("Enter principal"))
r=float(input("Enter rate"))
t=float(input("Enter time"))
si=(p*r*t)/100
ci=p*((1+r/100)**t-1)
print("Simple Interest =", si)
print("Compound Interest =", ci)
print("Compound Interest - Simple Interest =", ci-si)
