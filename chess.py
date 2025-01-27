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
mp.yticks(range(8),labels=[f'i' for i in range(1,9)])
x=str(input("letter a-h : "))
y = int(input("number 1-8 : "))
circle = mp.Circle((x,y) , radius=(0.2))
ax.add_patch(circle)
mp.show()
