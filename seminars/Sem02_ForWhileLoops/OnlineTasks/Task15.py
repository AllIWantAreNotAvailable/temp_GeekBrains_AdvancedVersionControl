"""Задача №15:
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно,
что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много
и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на
новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза

Input:
-   5 -> 5 1 6 5 9
Output:
-   1 9
"""


from random import randint, random


watermelons_total = int(input('Сколько арбузов лежит на прилавке, шт?\n>>> '))
watermelons_weights = [randint(0, 158) + random() for _ in range(watermelons_total)]
min_weight, max_weight = watermelons_weights[0], watermelons_weights[0]

for i in range(1, len(watermelons_weights)):
    watermelon = watermelons_weights[i]
    if watermelon < min_weight:
        min_weight = watermelon
    if max_weight < watermelon:
        max_weight = watermelon

print(f'Выбрали арбуз весом {min_weight:.3F} кг для тёщи.\n'
      f'Выбрали арбуз весом {max_weight:.3F} кг для себя.')
