import random
food_storage = 20
class Animal:
    age = 0
    satiety = 100
    def __init__(self, name, name_specie, sex):
        self.sex = sex
        self.name = name
        self.specie = name_specie
        if self.specie == "A":
            self.food = ["B", "C"]
            self.habitat = "earth"
            self.lifespan = 20
            self.size = 5
        elif self.specie == "B":
            self.food = "grass"
            self.habitat = "earth"
            self.lifespan = 20
            self.size = 6
        elif self.specie == "C":
            self.food = "grass"
            self.habitat = "earth"
            self.lifespan = 20
            self.size = 7
        elif self.specie == "D":
            self.food = "grass"
            self.habitat = "earth"
            self.lifespan = 20
            self.size = 8
        elif self.specie == "E":
            self.food = ["F", "G"]
            self.habitat = "water"
            self.lifespan = 20
            self.size = 5
        elif self.specie == "F":
            self.food = "grass"
            self.habitat = "water"
            self.lifespan = 20
            self.size = 9
        elif self.specie == "G":
            self.food = "grass"
            self.habitat = "water"
            self.lifespan = 20
            self.size = 2
        elif self.specie == "H":
            self.food = "grass"
            self.habitat = "water"
            self.lifespan = 20
            self.size = 5
        elif self.specie == "I":
            self.food = ["J", "K"]
            self.habitat = "air"
            self.lifespan = 20
            self.size = 3
        elif self.specie == "J":
            self.food = "grass"
            self.habitat = "air"
            self.lifespan = 20
            self.size = 2
        elif self.specie == "K":
            self.food = "grass"
            self.habitat = "air"
            self.lifespan = 20
            self.size = 1
        elif self.specie == "L":
            self.food = "grass"
            self.habitat = "air"
            self.lifespan = 20
            self.size = 2
    def info(self):
        print("пол:", self.sex, "возраст:", self.age, "сытость:", self.satiety, "%")
    def reproduction(self, partner):
        if self.specie != partner.specie:
            return "эти животные разных видов"
        if self.sex == partner.sex:
            return "животные должны быть разных полов"
        if self.habitat == "earth":
            if self.satiety <= 20 or partner.satiety <= 20:
                return "кто-то из животных голоден"
            if self.age < 6 or partner.age < 6:
                return "кто-то из животных слишком молод"
            print("родились 2 новые особи!")
            for i in range(1, 3):
                n = input("введите" + str(i) + "имя:")
                while n in cur_animals:
                    n = input("это имя занято, попробуйте ещё раз")
                cur_animals[n] = Animal(n, self.specie, random.choice(("m", "f")))
        elif self.habitat == "water":
            if self.satiety <= 50 or partner.satiety <= 50:
                return "кто-то из животных голоден"
            print("родились 10 новых особей!")
            for i in range(1, 11):
                n = input("введите" + str(i) + "имя:")
                while n in cur_animals:
                    n = input("это имя занято, попробуйте ещё раз")
                cur_animals[n] = Animal(n, self.specie, random.choice(("m", "f")))
        elif self.habitat == "air":
            if self.satiety <= 42 or partner.satiety <= 42:
                return "кто-то из животных голоден"
            if self.age < 4 or partner.age < 4:
                return "кто-то из животных слишком молод"
            print("родились 4 новые особи!")
            for i in range(1, 5):
                n = input("введите" + str(i) + "имя:")
                while n in cur_animals:
                    n = input("это имя занято, попробуйте ещё раз")
                cur_animals[n] = Animal(n, self.specie, random.choice(("m", "f")))
        return ""
                

def information():
    print("на данной планете существует 12 видов животных:")
    print("A : питается животными видов B и C, живёт на земле, продолжительность жизни 20")
    print("B : питается травой, живёт на земле, продолжительность жизни 20")
    print("C : питается травой, живёт на земле, продолжительность жизни 20")
    print("D : питается травой, живёт на земле, продолжительность жизни 20")
    print("E : питается животными видов F и G, живёт в воде, продолжительность жизни 20")
    print("F : питается травой, живёт в воде, продолжительность жизни 20")
    print("G : питается травой, живёт в воде, продолжительность жизни 20")
    print("H : питается травой, живёт в воде, продолжительность жизни 20")
    print("I : питается животными видов J и K, живёт в воздухе, продолжительность жизни 20")
    print("J : питается травой, живёт в воздухе, продолжительность жизни 20")
    print("K : питается травой, живёт в воздухе, продолжительность жизни 20")
    print("L : питается травой, живёт в воздухе, продолжительность жизни 20")
def helpp():
    print("команды:")
    print("/add - добавление особи")
    print("/finish - закончить работу программы")
    print("/food - узнать количество растительной пищи на планете")
    print("/changefood - увеличить количество растительной пищи на планете")
    print("/info - выводит информацию об особи")
    print("/sex - размножение")
    print("/plustime - увеличить время на 1")
    print("/animals - выводит информацию о всех живых животных")
def time_plus():
    global food_storage
    deaths = []
    for i in cur_animals:
        cur_animals[i].age += 1
        if cur_animals[i].lifespan < cur_animals[i].age:
            food_storage += cur_animals[i].size
            print("особь " + cur_animals[i].name + " умерла")
            deaths.append(i)
        else:
            if cur_animals[i].food == "grass":
                if food_storage > 0:
                    food_storage -= 1
                    cur_animals[i].satiety += 0.26 * cur_animals[i].satiety 
                    if cur_animals[i].satiety > 100: cur_animals[i].satiety = 100
                else:
                    cur_animals[i].satiety -= 0.09 * cur_animals[i].satiety
            else:
                cur_animals[i].satiety -= 0.09 * cur_animals[i].satiety
                for j in cur_animals:
                    if cur_animals[j].specie in cur_animals[i].food:
                        r = random.choice((1, 0))
                        if r == 1:
                            cur_animals[i].satiety += 0.62 * cur_animals[i].satiety
                            if cur_animals[i].satiety > 100: cur_animals[i].satiety = 100
                            print("особь " + cur_animals[j].name + " съели")
                            deaths.append(j)
                            break
                        else:
                            cur_animals[i].satiety -= 0.16 * cur_animals[i].satiety
    for i in deaths:
        del cur_animals[i]
    for i in cur_animals:
        if cur_animals[i].satiety < 10:
            print("особь " + cur_animals[i].name + " умерла")
            del cur_animals[i]
    return
                            
def inf():
    global cur_animals, food_storage
    print("живые животные:")
    for i in cur_animals:
        print(cur_animals[i].name)
        cur_animals[i].info()
                
                
species = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
cur_animals = dict()
time = 0
command = 0
information()
helpp()
while command != "/finish":
    command = input()
    if command == "/add":
        a = input("введите имя особи:")
        while a in cur_animals:
            a = input("это имя занято, попробуйте ещё раз:")
        b = input("введите вид особи:")
        while b not in species:
            b = input("такого вида не существует, попробуйте ещё раз:")
        c = input("введите пол особи(m или f):")
        while c not in ["m", "f"]:
            c = input("такого пола не существует, попробуйте ещё раз:")
        cur_animals[a] = Animal(a, b, c)
    elif command == "/food":
        print("количество растительной пищи на планете:", food_storage)
    elif command == "/changefood":
        a = input()
        while not a.isnumeric():
            a = input("введите число")
        food_storage += int(a)
    elif command == "/info":
        a = input("введите имя особи:")
        while a not in cur_animals:
            a = input("такой особи не существует, попробуйте ещё раз:")
        cur_animals[a].info()
    elif command == "/sex":
        a = input("введите имя особи:")
        b = input("введите имя особи:")
        while a not in cur_animals or b not in cur_animals:
            print("такой особи не существует, попробуйте ещё раз:")
            a = input("введите имя особи:")
            b = input("введите имя особи:")
        print(cur_animals[a].reproduction(cur_animals[b]))
    elif command == "/plustime":
        time_plus()
        time += 1
    elif command == "/animals":
        inf()
        
        







