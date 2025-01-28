# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.colors
fig, ax = mp.subplots()
letters = ['a','b','c','d','e','f','g','h']
board= np.array([[1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1], [1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1] ,[1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0], [0,1,0,1,0,1,0,1]])
mp.imshow(board,cmap='hot')
mp.title("Chess board")
mp.xticks(range(8) , labels=letters)
mp.yticks(range(8),labels=[f'{i}' for i in range(1,9)])
x=ord(input("letter a-h : "))-96
print(x)
y = float(input("number 1-8 : "))
circle = mp.Circle((x-1,y-1) , radius=(0.2), color = "pink")
for ferz in range(8):
    #up/down
    if ferz != y-1:
        circle1 = mp.Circle((x - 1, ferz), radius=(0.1), color="purple")
        ax.add_patch(circle1)
    if ferz != x-1:
        circle2 = mp.Circle((ferz, y-1), radius=(0.1), color="purple")
        ax.add_patch(circle2)
    #diagonally
    circle3 = mp.Circle((x - 1 + ferz, y-1 + ferz), radius=(0.1), color="purple")
    ax.add_patch(circle3)
    circle4 = mp.Circle((x - 1 - ferz, y - 1 + ferz), radius=(0.1), color="purple")
    ax.add_patch(circle4)
    circle5 = mp.Circle((x - 1 + ferz, y - 1 - ferz), radius=(0.1), color='purple')
    ax.add_patch(circle5)
    circle6 = mp.Circle((x - 1 - ferz, y - 1 - ferz), radius=(0.1), color="purple")
    ax.add_patch(circle6)

ax.add_patch(circle)
mp.show()
