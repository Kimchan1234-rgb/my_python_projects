import random 

zagadannoe = random.randint(1, 10)
popytki = 0

print("Я загадал число от 1 до 10!")
print("Попробуй угадать!")

while True:
    guesss = int(input("Твоя догадка: "))
    popytki += 1
    
    if guesss < zagadannoe:
        print("Больше!")
    elif guesss > zagadannoe:
        print("Меньше!")
    else:
        print(f"Правильно! Ты угадал за {popytki} попыток! ")
        break

    

    