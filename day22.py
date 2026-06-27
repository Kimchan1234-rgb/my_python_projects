produkty =  ["хлеб", "молоко", "яйца", "масло"]

print(produkty)

print(produkty[0])
print(produkty[-1])

print(len(produkty))

for produkt in produkty:
    print(f"Купить: {produkt}")

produkty.append("сыр")
print(produkty)

produkty.remove("молоко")
print(produkty)

produkty.sort()
print(produkty)

if "хлеб" in produkty:
    print("Хлеб в списке есть!")