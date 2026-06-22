# Типы данных в Python
vozrast = 34
rost = 182.2
imya = "Denis"
online = True

# Проверяем тип каждой переменной
print(type(vozrast))
print(type(rost))
print(type(imya))
print(type(online))

# Преобразование типов
vozrast_str = str(vozrast)
print(type(vozrast_str))

chislo = int("25")
print(type(chislo))
print(chislo + 5)

print(f"Меня зовут {imya}, мне {vozrast} лет")