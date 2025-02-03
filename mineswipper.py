# Задача:
# Создайте игровое поле для "Сапёра" размером 10×10.
# Поле должно быть представлено в виде двумерного массива.
# Разместите 15 мин случайным образом (обозначьте их числом −1).
# Для каждой клетки без мины подсчитайте количество мин в соседних клетках.
# Визуализируйте:
# Само поле (где мины выделены красным).
# Поле с числами, где указано количество мин вокруг каждой клетки (для наглядности).
#
import numpy as np
import matplotlib.pyplot as mp

fig, ax = mp.subplots()
playboard = np.array([[1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1], [1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1] ,[1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1], [1,0,1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1,0,1]])
mp.imshow(playboard,cmap='hot')
mp.title('sapper')
mp.xticks(range(10) , labels=[f'{i}' for i in range(1,11)])
mp.yticks(range(10),labels=[f'{i}' for i in range(1,11)])


mina1x = np.random.randint(1, 11)
mina1y = np.random.randint(1, 11)
x1 = mina1x
y1 = mina1y
firstmina = mp.Circle((x1-1,y1-1) , radius=(0.2), color = 'red')
ax.add_patch(firstmina)
nelzya=[]
for i in range(14):
    mina2x = np.random.randint(1, 11)
    mina2y = np.random.randint(1, 11)
    x2 = mina2x
    y2 = mina2y
    if x2 != x1:
        secondmina = mp.Circle((x2 - 1, y2 - 1), radius=(0.2), color="red")
        ax.add_patch(secondmina)
    else:
        while x2!=x1:
            x2 = np.random.randint(1, 11)
        secondmina = mp.Circle((x2 - 1, y2 - 1), radius=(0.2), color="red")
        ax.add_patch(secondmina)

mp.show()

































#''mina2x=np.random.randint(1,11,)
#mina2y=np.random.randint(1,11)
#x2=mina2x
#y2=mina2y
#mina3x=np.random.randint(1,11,)
#mina3y=np.random.randint(1,11)
#x3=mina3x
#y3=mina3y
#mina4x=np.random.randint(1,11,)
#mina4y=np.random.randint(1,11)
#x4=mina4x
#4=mina4y
#mina5x=np.random.randint(1,11,)
#mina5y=np.random.randint(1,11)
#x5=mina5x
#=mina5y
#mina6x=np.random.randint(1,11,)
#mina6y=np.random.randint(1,11)
#x6=mina6x
#y6=mina6y