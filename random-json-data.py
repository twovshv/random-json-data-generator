import random as rnd
import json
import sys
import datetime as dt

#Инициализация
def writeToFile(filePath, text):
    print(f"Производится запись сгенерированного json в файл {filePath}")
    with open(filePath, 'w') as file:
        file.write(text)

def genMobPhoneRand():
    phoneNum='+7'
    for i in range(10): phoneNum+=str(rnd.randrange(10))
    return phoneNum

def genBirthyear():
    nowYear = dt.datetime.now().year
    return rnd.randrange(nowYear-100, nowYear+1)
 
def simpleTransliterateRusToEn(word):
    word = word.lower()
    dictLiters = {
            'а':'a', 
            'б': 'b',
            'в': 'v',
            'г': 'g',
            'д': 'd',
            'е': 'e',
            'ё': 'e',
            'ж': 'zh',
            'з': 'z',
            'и': 'i',
            'й': 'y',
            'к': 'k',
            'л': 'l',
            'м': 'm', 
            'н': 'n',
            'о': 'o',
            'п': 'p',
            'р': 'r',
            'с': 's',
            'т': 't',
            'у': 'u',
            'ф': 'f',
            'х': 'h',
            'ц': 'c',
            'ч': 'ch',
            'ш': 'sh',
            'щ': 'shch',
            'ъ': '',
            'ы': 'y', 
            'ь': '',
            'э': 'e', 
            'ю': 'u',
            'я': 'ya'
    }
    translit=''

    for i in word:
        translit+=dictLiters[i]
    
    return translit

def genEmail(lastName, firstName, birthyear):
    methodInd = rnd.randrange(3)
    domain = rnd.choice(("yandex.ru", "mail.ru", "gmail.com"))
    email = ''
    match methodInd:
        case 0:
            email = simpleTransliterateRusToEn(lastName)+simpleTransliterateRusToEn(firstName[0])+str(birthyear)
        case 1:
            email = simpleTransliterateRusToEn(firstName)+simpleTransliterateRusToEn(lastName[0])+str(birthyear)
        case 2:
            email = simpleTransliterateRusToEn(lastName)+simpleTransliterateRusToEn(firstName)
    email+=f"@{domain}"
    return email


jsonRes=[]

lastNameM = ["Васечкин", "Петров", "Сидоров", "Кожемяков", "Аскользкий", "Баринов", "Волынов", "Гусев", "Деревянко", "Ежов", "Изваров", "Коломыйцев", "Лебедев", "Марков", "Носов", "Котов"]
firstNameM = ["Василий", "Петр", "Владимир", "Константин", "Борис", "Антон", "Валерий", "Михаил", "Олег", "Александр", "Тимофей", "Максим", "Павел", "Юрий", "Даниил", "Сергей", "Андрей", "Алексей"]
lastNameF = ["Анютова", "Котейкина", "Сокольникова", "Мясоедова", "Лопатина", "Зарубина", "Смородинова", "Павлова", "Кузнецова", "Сидорова", "Мельникова", "Виноградова", "Морозова", "Ковалёва"]
firstNameF = ["Елена", "Ирина", "Мария", "Юлия", "Анастасия", "Виктория", "Екатерина", "Дарья", "Ирина", "Елизавета", "Лариса", "Вера",  "Анна", "Любовь", "Людмила", "Надежда", "Наталья", "Ольга", "Нина"]
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
        LNRand = rnd.choice(lastNameM)
        FNRand = rnd.choice(firstNameM)
    else:
        LNRand = rnd.choice(lastNameF)
        FNRand = rnd.choice(firstNameF)
    cityRand = rnd.choice(city)
    mobPhoneRand = genMobPhoneRand()
    birtyear = genBirthyear()
    email = genEmail(LNRand, FNRand, birtyear)
    jsonRes.append({
            "LastName": LNRand,
            "FirstName": FNRand,
            "Gender": gendRand,
            "City": cityRand,
            "Mobile Phone Number": mobPhoneRand,
            "Email": email,
            "Birth year": birtyear
            })

#Вывод результата
print("JSON:\n")
if filePath:
    writeToFile(filePath, json.dumps(jsonRes, ensure_ascii=False))
else:
    print(json.dumps(jsonRes, ensure_ascii=False))
