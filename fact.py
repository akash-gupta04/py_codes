n = int(input("\nEnter a number:"))
i = 1
fact = 1
while(i<=n):
    fact = fact * i
    i = i + 1
print("\nFactorial of ",n,"is ",fact)