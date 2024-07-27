out = open("filtered_cities.txt", "w")
try:
    f = open("cities.txt")
except FileNotFoundError:
    out.write("файла не существует")
else:
    a = f.readlines()
    a.sort()
    n = int(input())
    for i in a:
        r = i.strip().split(":")
        if int(r[1]) > n:
            out.write(r[0] + "\n")
    f.close()
out.close()
