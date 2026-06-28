# Словарь — данные парами ключ: значение
kontakt = {
    "imya": "Denis",
    "vozrast": 34,
    "gorod": "Poltava",
    "online": True
}

# Вывести весь словарь
print(kontakt)

# Получить значение по ключу
print(kontakt["imya"])
print(kontakt["gorod"])

# Добавить новый ключ
kontakt["telefon"] = "+380501234567"
print(kontakt)

# Проверить есть ли ключ
if "telefon" in kontakt:
    print(f"Телефон: {kontakt['telefon']}")

# Перебрать все пары
for klyuch, znachenie in kontakt.items():
    print(f"{klyuch}: {znachenie}")