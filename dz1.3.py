def sum(n):
    f = 0
    while n > 0:
        f += n % 10
        n //= 10
    return f
n = int(input())
while n > 9:
    n = sum(n)
print(n)
