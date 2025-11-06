import random as rnd
import json
import sys

#Инициализация
def writeToFile(filePath, text):
    print(f"Производится запись сгенерированного json в файл {filePath}")
    with open(filePath, 'w') as file:
        file.write(text)

jsonRes={}

firstNameM = ["Васечкин", "Петров", "Сидоров", "Кожемяков", "Аскользкий", "Баринов", "Волынов", "Гусев", "Деревянко", "Ежов", "Изваров", "Коломыйцев", "Лебедев", "Марков", "Носов", "Котов"]
lastNameM = ["Василий", "Петр", "Владимир", "Константин", "Борис", "Антон", "Валерий", "Михаил", "Олег", "Александр", "Тимофей", "Максим", "Павел", "Юрий", "Даниил", "Сергей", "Андрей", "Алексей"]
firstNameF = ["Анютова", "Котейкина", "Сокольникова", "Мясоедова", "Лопатина", "Зарубина", "Смородинова", "Павлова", "Кузнецова", "Сидорова", "Мельникова", "Виноградова", "Морозова", "Ковалёва"]
lastNameF = ["Елена", "Ирина", "Мария", "Юлия", "Анастасия", "Виктория", "Екатерина", "Дарья", "Ирина", "Елизавета", "Лариса", "Вера",  "Анна", "Любовь", "Людмила", "Надежда", "Наталья", "Ольга", "Нина"]
city = ["Воронеж", "Москва", "Санкт-Петербург", "Волгоград", "Кисловодск", "Белгород", "Калуга", "Новосибирск", "Самара", "Казань", "Челябинск", "Ростов-на-Дону", "Уфа", "Екатеринбург", "Омск", "Нижний Новгород"]
old = range(101)
gender = ["Мужчина", "Женщина"]

#Работа с аргументами
resCount = 1
filePath = False
try:
    args = sys.argv
    for i, el in enumerate(args):
        if "--count" == args[i].split("=")[0]:
            resCount = int(args[i].split("=")[1])
        elif "--file" == args[i].split("=")[0]:
            filePath = args[i].split("=")[1]
except IndexError:
    resCount = 1
    filePath = False
print(f"ARGS:\n\tcount:{resCount}\n\tfilePath:{filePath}")

#Генерация
for i in range(resCount):
    gendRand = rnd.choice(gender)
    if gendRand == gender[0]:
        FNRand = rnd.choice(firstNameM)
        LNRand = rnd.choice(lastNameM)
    else:
        FNRand = rnd.choice(firstNameF)
        LNRand = rnd.choice(lastNameF)
    cityRand = rnd.choice(city)
    oldRand = rnd.choice(old)
    jsonRes[i] = {
            "FirstName": FNRand,
            "LastName": LNRand,
            "Gender": gendRand,
            "City": cityRand,
            "Old": oldRand
            }

#Вывод результата
print("JSON:\n")
if filePath:
    writeToFile(filePath, json.dumps(jsonRes, ensure_ascii=False))
else:
    print(json.dumps(jsonRes, ensure_ascii=False))
