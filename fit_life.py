""" Проект FitLife - MVP версия 1.0 """
water_per_kg = 30
volume_water_ml = 1000

# запрос имени
user_name = input('Введите своё имя:')


# запрос возраста
user_age = int(input('Введите свой возраст:'))


# запрос веса
user_weght = float(input('Введите свой вес:'))


# запрос роста
user_height = float(input('Введите свой рост в метрах, (например: 1.75):'))


# расчёт индекса массы тела
bmi = user_weght / (user_height ** 2)
round(bmi, 1)


# расчёт нормы воды в литрах
water_ml = user_weght * water_per_kg
water_l = water_ml / volume_water_ml

# вывод результата с помощью f-строк
print(f'Привет, {user_name}!\nТебе {user_age} лет')
print(f'Твой индекс массы тела: {bmi:.1f} кг/м²')
print(f'Рекомендуемая норма воды: {water_l:.1f} л. в день')
print("Расчет окончен. Будьте здоровы!")
