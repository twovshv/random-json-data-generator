import random as rnd
import json
import sys
import datetime as dt
import argparse 

# Запись в файл
def writeToFile(filePath, text):
    print(f"Производится запись сгенерированного json в файл {filePath}")
    with open(filePath, 'w') as file:
        file.write(text)

# Генерация случайного номера мобильного телефона
def genMobPhoneRand():
    phoneNum='+7'
    for i in range(10): phoneNum+=str(rnd.randrange(10))
    return phoneNum

# Генерация даты рождения 
def genBirthyear():
    nowYear = dt.datetime.now().year
    return rnd.randrange(nowYear-100, nowYear+1)
 
# Простая транслитерация РУС->АНГЛ
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

# Генерация случайного адреса электронной почты
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


def main():
     
    jsonRes=[]
    lastNameM = ["Васечкин", "Петров", "Сидоров", "Кожемяков", "Аскользкий", "Баринов", "Волынов", "Гусев", "Деревянко", "Ежов", "Изваров", "Коломыйцев", "Лебедев", "Марков", "Носов", "Котов"]
    firstNameM = ["Василий", "Петр", "Владимир", "Константин", "Борис", "Антон", "Валерий", "Михаил", "Олег", "Александр", "Тимофей", "Максим", "Павел", "Юрий", "Даниил", "Сергей", "Андрей", "Алексей"]
    lastNameF = ["Анютова", "Котейкина", "Сокольникова", "Мясоедова", "Лопатина", "Зарубина", "Смородинова", "Павлова", "Кузнецова", "Сидорова", "Мельникова", "Виноградова", "Морозова", "Ковалёва"]
    firstNameF = ["Елена", "Ирина", "Мария", "Юлия", "Анастасия", "Виктория", "Екатерина", "Дарья", "Ирина", "Елизавета", "Лариса", "Вера",  "Анна", "Любовь", "Людмила", "Надежда", "Наталья", "Ольга", "Нина"]
    city = ["Воронеж", "Москва", "Санкт-Петербург", "Волгоград", "Кисловодск", "Белгород", "Калуга", "Новосибирск", "Самара", "Казань", "Челябинск", "Ростов-на-Дону", "Уфа", "Екатеринбург", "Омск", "Нижний Новгород"]
    old = range(101)
    gender = ["Мужчина", "Женщина"]

   #Работа с аргументами
    parser = argparse.ArgumentParser(
                description='',
                formatter_class=argparse.RawDescriptionHelpFormatter,
                epilog="""
                       Примеры использования:
                        """
            )        
    parser.add_argument('--count', required=False, type=int, default=1, help='Количество объектов в выходном JSON')
    parser.add_argument('--file', required=False, type=str, help='Путь к файлу, куда требуется записать json')
    args = parser.parse_args()
    resCount=args.count
    filePath=args.file

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

if __name__=="__main__":
    try:
        main()
    except Exception as E:
        print(f"Неизвестная ошибка: {e}")
