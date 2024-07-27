out = open("output.txt", "w")
try:
    f = open("input.txt")
except FileNotFoundError:
    out.write("файла не существует")
else:
    a = f.readlines()
    d = input()
    sl = dict()
    for i in a:
        s = i.replace(" ", "")
        name = s.strip().split(":")
        course = name[1].split(",")
        for j in course:
            if j in sl:
                if name[0] not in sl[j]:
                    sl[j].append(name[0])
            else:
                sl[j] = [name[0]]
    for i in sl[d]:
        out.write(i + "\n")
    f.close()
out.close()
