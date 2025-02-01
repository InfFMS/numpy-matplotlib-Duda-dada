# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
import numpy as np
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

n=0
for i in range(len(throws)-1):
    if throws[i]==throws[i+1]:
        n+=1
    else:
        the_same_elements=n
        n=0
print(the_same_elements)




