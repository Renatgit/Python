import random

n=int(input('Введите количество элементов: '))
arr=[random.randint(0, 15) for i in range(n)]

print(arr)
print(f"Первый элемент списка: {arr[0]}\nВторой элемент списка: {arr[-1]}")

p=1
for i in arr:
   p*=i
print(f"Произведение всех чисел: {p}")
