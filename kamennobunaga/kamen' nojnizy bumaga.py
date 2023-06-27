import random

random_number = random.randint(1, 3)
player_guess = input('Напиши (Камень, ножницы, бумага): ')

if random_number == 1:
    computer_guess = "камень"
elif random_number == 2:
    computer_guess = "ножницы"
else:
    computer_guess = "бумага"

if player_guess == computer_guess:
    print('Ничья! Компьютер выбрал', computer_guess)
elif (
        (player_guess == "камень" and computer_guess == "ножницы") or
        (player_guess == "ножницы" and computer_guess == "бумага") or
        (player_guess == "бумага" and computer_guess == "камень")
):
    print('Ты победил! Компьютер выбрал', computer_guess)
else:
    print('Ты проиграл! Компьютер выбрал', computer_guess)