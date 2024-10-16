name = (input("Здравствуйте, введите Ваше имя: "))
print("Приветствую Вас, на нашей платформе", name)
print("Для того, чтобы программа сработала, вам нужно вписать 3 ЦЕЛЫХ числа")  #first, second, third
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третие число: "))
if first == second == third:
    print("Все числа равны между собой(3)")
elif first == second:
    print("Имеются 2 одинаковых числа(2)")

elif first == third:
    print("Имеются 2 одинаковых числа(2)")

elif second == third:
    print("Имеются 2 одинаковых числа(2))")

else:
    print(name,", данные числа не подходят по условиям(0)")
# проверка на запись данных
st1 = {name: first}
print(st1)
rd2 = {name: second}
print(rd2)
thd3 = {name: third}
print(thd3)