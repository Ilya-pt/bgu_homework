def f(a):
    if a < 2:
        return 1
    return f(a-1) + f(a-2)
n = int(input())
print(f(n))
