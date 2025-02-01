# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import category

temperature=np.random.randint(-40,35,365)
count_el=len(temperature)
medium_tempreture=sum(temperature)/count_el
print(round(medium_tempreture, 1)) #округлили до дсятых
hot_days=0
for i in temperature:
    if i>25:
        hot_days+=1
print(hot_days)

