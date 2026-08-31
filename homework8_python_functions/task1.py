MAX_RENTAL_BATCH_LIMIT = 150.0

def calculate_rental_batch(quantity: int, rental_rate: float, discount: float = 0.0) -> tuple:
    """
     quantity - represents quantity of discs
     rental_rate - represents price of renting disc
     discount - represents discount for specific genre 
     function returns tuple of final sum and whether or not is limit exceeded
    """

    final_sum = round(quantity * rental_rate * (1 - discount), 2)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT

    return (final_sum, is_limit_exceeded)

batch_1 = 'Academy Dinosaur'
batch_1_arguments = calculate_rental_batch(30, 2.99)  # positional arguments
batch_2 = 'Affair Prejudice'
batch_2_arguments = calculate_rental_batch(quantity=40, rental_rate=4.99, discount=0.1)  # keyword arguments
batch_3 = 'Agent Truman'
batch_3_arguments = calculate_rental_batch(rental_rate=1.99, quantity=10)
batch_4 = 'African Egg'
batch_4_arguments = calculate_rental_batch(50, rental_rate=3.50, discount=0.2)

print('=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===')

print(f'Партия 1 ({batch_1}): Сумма {batch_1_arguments[0]}$. Превышение лимита: {batch_1_arguments[1]}')
# Партия 1 (Academy Dinosaur): Сумма 89.7$. Превышение лимита: False
print(f'Партия 2 ({batch_2}): Сумма {batch_2_arguments[0]}$. Превышение лимита: {batch_2_arguments[1]}')
# Партия 2 (Affair Prejudice): Сумма 179.64$. Превышение лимита: True
print(f'Партия 3 ({batch_3}): Сумма {batch_3_arguments[0]}$. Превышение лимита: {batch_3_arguments[1]}')
# Партия 3 (Agent Truman): Сумма 19.9$. Превышение лимита: False
print(f'Партия 4 ({batch_4}): Сумма {batch_4_arguments[0]}$. Превышение лимита: {batch_4_arguments[1]}')
# Партия 4 (African Egg): Сумма 140.0$. Превышение лимита: False
