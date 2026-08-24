# Calculator programme which takes two real numbers and output the result of chosen operation
first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))
print('Выберите оператор (+, -,*, /): ', end='')
operator = input()

if operator == '+':
    print(f'Результат: {first_number} + {second_number} = {first_number + second_number}')
elif operator == '-':
    print(f'Результат: {first_number} - {second_number} = {first_number - second_number}') 
elif operator == '*':
    print(f'Результат: {first_number} * {second_number} = {first_number * second_number}')
elif operator == '/':

    if second_number == 0:
        raise ValueError('Cannot divide by zero')
    
    print(f'Результат: {first_number} / {second_number} = {first_number / second_number}')
else:
    raise ValueError('Wrong operator')
