# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import category

throws=np.random.randint(1,7,1000)
#print(throws)
one=0
two=0
three=0
four=0
five=0
six=0
for i in (throws):
    if i == 1:
        one+=1
    if i == 2:
        two+=1
    if i == 3:
        three+=1
    if i == 4:
        four+=1
    if i == 5:
        five+=1
    if i == 6:
        six+=1
#print (one,two,three,four,five,six)
probability1 = one/10
probability2 = two/10
probability3 = three/10
probability4 = four/10
probability5 = five/10
probability6 = six/10
#print('вероятность единицы:', probability1,'%','вероятность двойки:', probability2, '%','вероятность тройки:', probability3,'%', 'вероятность четверки:', probability4,'%','вероятность пятерки:' , probability5,'%','вероятность шестерки:', probability6,'%')
ma=0
the_same_elements=0
n=0
for i in range(len(throws)-1):
    if throws[i]==throws[i+1]:
        the_same_elements+=1
    else:
        if the_same_elements>ma:
            ma=the_same_elements
        the_same_elements=0


categories = ["one","two","three","four","five","six"]
values = [one, two, three, four, five,six]
plt.bar(categories, values, color='pink')
plt.title("Количество каждого полученного результата")
ax=plt.subplots()
#plt.legend(["one="],'one',["two="],'two',["three="],'three',["four"],'four',["five"],'five',["six"],'six'))
categories = ["one","two","three","four","five","six"]
values = [probability1,probability2,probability3,probability4,probability5,probability6]
plt.bar(categories, values, color='pink')
plt.title("Вероятность выпадения каждого значения(%)")
#ax=plt.subplots()
plt.show()
print(throws)
print("Сколько раз встречается единица:",
one,"Сколько раз встречается двойка:", two,"Сколько раз встречается тройка:",three,"Сколько раз встречается четверка:",
four,"Сколько раз встречается пятерка:", five, "Сколько раз встречается шестерка:",six)
print('вероятность единицы:', probability1,'%','вероятность двойки:', probability2, '%','вероятность тройки:', probability3,'%',
'вероятность четверки:', probability4,'%','вероятность пятерки:' , probability5,'%','вероятность шестерки:', probability6,'%')
print('Максимальное количество идущих подряд одинаковых элементов:', ma)

