# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]



a = list(map(int, input('ВВедите список: ').split()))
x = len(a)
print(x)
if x % 2 == 0 :

   b = a[:len(a)//2]
   d = a[len(a)//2:]
   d.reverse()
   print(b)
   print(d)
   for i in range(0,len(d)):
       print(b[i]*d[i],end = ' ')
else:
   b = a[:(len(a)//2)+1]
   d = a[len(a)//2:]
   d.reverse()
   print(b)
   print(d)
   for i in range(0,len(d)):
       print(b[i]*d[i], end = ' ')