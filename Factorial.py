def faculteit(n):
    if n == 1 or n==0:
        return 1
    else:
        return n * faculteit(n-1)

aantal = int(input())
for i in range(1, aantal+1):
    getal = int(input())
    if getal > 13:
        print("input too large")
    else:
        print(faculteit(getal))
