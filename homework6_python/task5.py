# Game "Guess a number"
import random

random_number = random.randint(1, 20)
print('Я загадал число от 1 до 20. У тебя 5 попыток!')

attempt = 1
while attempt <= 5:
    print(f'Попытка {attempt}.', end=' ')
    guess_number = int(input('Введите число: '))

    if guess_number < random_number:
        print(f'Слишком мало! Осталось попыток: {5 - attempt}')
    elif guess_number > random_number:
        print(f'Слишком много! Осталось попыток: {5 - attempt}')
    else:
        print('Ты угадал! Отличная работа')
        break

    attempt += 1

else:
    print('Попытки закончились! Ты не угадал :(')
          