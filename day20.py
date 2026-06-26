# Программа - определи время суток
chas = int(input("Введи текущий час (0-23): "))

if chas >= 6 and chas < 12:
    print("Доброе утро!")
elif chas >= 12 and chas < 18:
    print("Добрый день!") 
elif chas >= 18 and chas <23:
    print("Добрый вечер!")
else:
    print("Доброй ночи!")

# Программа - можно ли водить машину
vozrast = int(input("Введи свой возраст: "))
prava = input("Есть ли у тебя права? (да/нет): ")

if vozrast >= 18 and prava == "да":
    print("Можешь водить машину!")
elif vozrast >= 18 and prava == "нет":
    print("Нужно получить права!")
else:
    print("Еще слишком молод для вождения!")
