f = open("input.txt")
out = open("output.txt", "w")
a = f.readlines()
check = {")":"(", "]":"[", "}":"{", ">":"<"}
m = ["[", "]", "{", "}", "(", ")", "<", ">"]
for i in a:
    n = []
    for j in i.strip():
        if j in m:
            n.append(j)
            if len(n) > 1 and n[-1] in check and check[n[-1]] == n[-2]:
                n.pop()
                n.pop()
    if len(n) == 0:
        out.write("true" + "\n")
    else:
        out.write("false" + "\n")
f.close()
out.close()
