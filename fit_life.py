# Проект FitLife - MVP версия 1.0


# запрос имени
user_name = input ('Введите своё имя:')


# запрос возраста
user_age = input ('Введите свой возраст:')
user_age_int = int(user_age)


# запрос веса
user_weght = input ('Введите свой вес:')
user_weght_float = float (user_weght)


# запрос роста
user_height = input ('Введите свой рост в метрах, (например: 1.75):')
user_height_float = float (user_height)


# расчёт индекса массы тела
bmi = user_weght_float / (user_height_float ** 2)
round (bmi, 1)


# расчёт нормы воды в литрах
water_per_kg = 30
water_ml = user_weght_float * water_per_kg
water_l = water_ml / 1000

# вывод результата с помощью f-строк
print (f'Привет, {user_name} {user_age_int} лет !')
print (f'Твой индекс массы тела: {bmi:.1f} кг/м²')
print (f'Рекомендуемая норма воды: {water_l:.1f} л. в день')
print("Расчет окончен. Будьте здоровы!")