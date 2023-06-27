import random

while True:
    bones = random.randint(1, 6)
    drop = input('Будете ли делать бросок? ')

    if drop == "да":
        print(bones)
    elif drop == "нет":
        print("Пока")
        break



