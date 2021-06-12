for i in range(1, 13):
    print(i, end="\t")
print()
print("---------------------------------------------------------------------------------\n")

for i in range(1, 11):
    for n in range(1, 11):
        print("\n")
        print(i * n, end="\t")
n = 1
while n <= 12:
    print("Table of ",n)
    i=1
    while i <= 10:
        print(n," * ",i," =  ",n*i)
        i = i + 1
    n = n + 1
