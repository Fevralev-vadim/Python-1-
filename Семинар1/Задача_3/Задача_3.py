# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных
# координат точек в этой четверти (x и y).

print('введите значение четверти ')
a = int (input())
if a==1:
    print('Диапазон возможных координат Х - от 0 до "+" бесконечности; Y - от 0 до "+" бесконечности')
elif a==2:
    print('Диапазон возможных координат Х - от 0 до "-" бесконечности; Y - от 0 до "+" бесконечности')
elif a==3:
    print('Диапазон возможных координат Х - от 0 до "-" бесконечности; Y - от 0 до "-" бесконечности')
elif a==4:
    print('Диапазон возможных координат Х - от 0 до "+" бесконечности; Y - от 0 до "-" бесконечности')
else:
    print('Нет такой четверти')