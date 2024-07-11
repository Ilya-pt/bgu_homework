out = open("output.txt", "w")
try:
    f = open("input.txt")
except FileNotFoundError:
    out.write("файла не существует")
else:
    a = f.readlines()
    s = 0
    for i in a:
        b = i.split(",")
        s += int(b[1])
    s /= len(a)
    for i in a:
        b = i.split(",")
        if int(b[1]) > s:
            out.write(b[0] + "\n")
            
    out.close()
    f.close()
out.close()
