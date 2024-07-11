out = open("output.txt", "w")
try:
    f1 = open("input1.txt")
    f2 = open("input2.txt")
except FileNotFoundError:
    out.write("файла не существует")
else:
    a = f1.readlines()
    b = f2.readlines()
    a.sort()
    b.sort()
    u1 = 0
    u2 = 0
    while u1 < len(a) and u2 < len(b):
        if a[u1] < b[u2]:
            out.write(a[u1].strip() + "\n")
            print(1)
            u1 += 1
        else:
            out.write(b[u2].strip() + "\n")
            print(1)
            u2 += 1
    if u1 == len(a):
        for i in range(u2, len(b)):
            out.write(b[i].strip() + "\n")
            print(1)
    else:
        for i in range(u1, len(a)):
            out.write(a[i].strip() + "\n")
            print(1)
        
    f1.close()
    f2.close()
out.close()
    
