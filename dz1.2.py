n = int(input())
a = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
b = ["", "десять", "двадцать ", "тридцать ", "сорок ", "пятьдесят ", "шестьдесят ", "семьдесят ", "восемьдесят ", "девяносто "]
c = ["", "сто ", "двести ", "триста ", "четыреста ", "пятьсот ", "шестьсот ", "семьсот ", "восемьсот ", "девятьсот "]
d = ["", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
n1 = n // 100
n2 = n % 100 // 10
n3 = n % 10
if n2 == 1 and n3 != 0:
    print(c[n1], d[n3], sep="")
else:
    print(c[n1], b[n2], a[n3], sep="")
