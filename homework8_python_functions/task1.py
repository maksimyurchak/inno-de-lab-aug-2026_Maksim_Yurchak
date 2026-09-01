MAX_RENTAL_BATCH_LIMIT = 150.0

def calculate_rental_batch(quantity: int, rental_rate: float, discount: float = 0.0) -> tuple[float, bool]:
    """
    Calculates the total rental price and checks if it exceeds the limit.

    Args:
        quantity: The number of discs to rent.
        rental_rate: The rental price per disc.
        discount: The discount percentage applicable to a specific genre.
            Defaults to 0.0.

    Returns:
        A tuple containing:
            - final_sum (float): The calculated final cost, rounded to two decimal places.
            - is_limit_exceeded (bool): True if the final cost is strictly greater
              than MAX_RENTAL_BATCH_LIMIT, False otherwise.
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
