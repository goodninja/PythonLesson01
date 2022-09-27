# Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Введите 0 или 1 для проверки истинности утверждения -> ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z: ')
x=int(input('Введите значение для X: '))
while x!=0 and x!=1:                        # проверка и ограничение на ввод, только 0 или 1
   x=int(input('Введите значение для X: ')) 
else: 
    y=int(input('Введите значение для Y: '))
    while y!=0 and y!=1:
        y=int(input('Введите значение для Y: '))
    else: 
        z=int(input('Введите значение для Z: '))
        while z!=0 and z!=1:
            z=int(input('Введите значение для Z: '))

firstFormula = not(x or y or z)
secondFormula = not x and not y and not z  
print('Производим проверку:') 
print(f'x = {x}, y = {y}, z = {z}') 
print(f'x or y or z = {x} или {y} или {z} = {x or y or z}')
print(f'not(x or y or z) = not {x or y or z} = {not x or y or z}')
print(f'not x = {not x}, not y = {not y}, not z = {not z}')
print(f'not x and not y and not z = {not x and not y and not z}')
print(f'{firstFormula} - {secondFormula}')
print('Результат:') 
if firstFormula == secondFormula:
    print('True')
else:
    print('False')