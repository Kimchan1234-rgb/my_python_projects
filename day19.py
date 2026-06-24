imya = input("Как тебя зовут?")
print(f"Привет, {imya}!")

vozrast = int(input("Сколько тебе лет? "))
print(f"Через 10 лет будет {vozrast + 10} лет")

rost = float(input("Какой твой рост в см? "))
print(f"Твой рост в метрах: {rost / 100}")

ves = float(input("Введи свой вес в кг: "))
rost_m = float(input("Введи свой рост в см: ")) / 100

imt = ves / (rost_m **2)
imt = round(imt, 1)

print(f"Твой ИМТ: {imt}")

if imt < 18.2:
    print("Недовес")
elif imt < 25:
    print("Норма")
elif imt < 30:
    print("Избыточный вес")
else:
    print("Ожирение")