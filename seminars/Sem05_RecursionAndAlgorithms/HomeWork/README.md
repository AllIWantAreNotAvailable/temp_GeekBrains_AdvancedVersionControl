***Общие комментарии по выполнению самостоятельной работы:***
> В ходе выполнения работы: поставленные задачи декомпозированы на методы (без фанатизма), основная логика запускается из точки входа и расположена в методе main(). К вынесенным из main() написана исчерпывающая документация.

> PS: Гиперссылки на соответсвующее директории репозитория GitHub привязаны к наименованиям маркеров вида **"Задача №*"**

> ***PSS:*** Буду рад оставленным комментариям и замечаниям по представленным решениям.

- [**Задача №26**](https://github.com/AllIWantIsNotAvailable/GeekBrains_IntroductionToPython/blob/main/seminars/Sem05_RecursionAndAlgorithms/HomeWork/Task26.py):

Комментарии к задаче:
> Написана рекурсивная функция с 2-мя параметрами, параметр 'base' статичен, а 'exponent' уменьшается на 1 в каждом следующем рекуррентном вызове, пока не достигнет значения 0 или 1.
> Ниже представлена основная логика решения:

```Python
def get_number_to_power(base: int, exponent: int) -> int:  
    """ Возвращает значение числа возведенного в степень.  
  
    :param base: Основание степени, <class 'int'>.
    :param exponent: Показатель степени, <class 'int'>.
    :return: Значение числа возведенного в степень, <class 'int'>.  
    """
	if exponent == 0:  
        return 1  
    elif exponent == 1:  
        return base  
    else:  
        return base * get_number_to_power(base, exponent - 1)
```


- [**Задача №28**](https://github.com/AllIWantIsNotAvailable/GeekBrains_IntroductionToPython/blob/main/seminars/Sem05_RecursionAndAlgorithms/HomeWork/Task28.py):

Комментарии к задаче:
> Написана рекурсивная функция с 2-мя параметрами. При решении соблюдено условие ограничения операций (+-1).
> В каждом следующем рекуррентном вызове параметры будут уменьшаться на 1, а возвращаемое значение представляется суммой 1 и рекуррентного вызова, кроме базового случая (оба параметры == 0). В базовом случае возвращается 0 как нейтральное число сложение и незначащая операция.
> Ниже представлена основная логика решения:

```Python
def get_sum_recursion(first_summand: int, second_summand: int) -> int:  
    """ Рекурсивная функция суммирования 2-х чисел.  
  
    :param first_summand: Первое слагаемое, <class 'int'>.
	:param second_summand: Второе слагаемое, <class 'int'>.
	:return: Сумма чисел, <class 'int'>.  
    """
	if first_summand:  
        return 1 + get_sum_recursion(first_summand - 1, second_summand)  
    elif second_summand:  
        return 1 + get_sum_recursion(first_summand, second_summand - 1)  
    else:  
        return 0
```


- [**Задача со звёздочкой №5**](https://github.com/AllIWantIsNotAvailable/GeekBrains_IntroductionToPython/blob/main/seminars/Sem05_RecursionAndAlgorithms/HomeWork/TaskStar05.py):

Комментарии к задаче:
> 2 цикла while: первый отвечает за ввод последовательности и останавливается при введенном 0; второй, удаляет из копии списка все максимальные элементы исходного.
> В инструкции возврата распаковываем исходный список в кортеж и последним элементом кортежа добавляем второй максимальный элемент.
> Основная логика ниже:

```Python
def get_second_biggest_number() -> tuple:  
    """ Возвращает 2-е по значение число вводимой последовательности и саму 
    последовательность.  
  
    :return: Последовательность чисел и второе по значение число, <class 'tuple'>  
    """
    cur_member = None  
    counter = 1  
    sequence = list()
      
    while cur_member != 0:  
        cur_member = int(input(f'Введите {counter} член '
						        'последовательности:\n>>> '))  
        sequence.append(cur_member)  
        counter += 1  
  
    first_biggest_index = max(sequence)  
    temp_sequence = sequence[:]
      
    while first_biggest_index in temp_sequence:  
        temp_sequence.remove(first_biggest_index)  
  
    return *sequence, max(temp_sequence)
```


- [**Задача со звёздочкой №6**](https://github.com/AllIWantIsNotAvailable/GeekBrains_IntroductionToPython/blob/main/seminars/Sem05_RecursionAndAlgorithms/HomeWork/TaskStar06.py):

Комментарии к задаче:
> Думаю, тут комментарии излишне: берем диапазон k-значных чисел, последовательно перебираем все и проверяем, равна ли сумма цифр очередного элемента искомой S.
> Основная логика ниже:

```Python
def get_numbers_sum_of_digits_equals_value(digits: int, sum_of_digits: int) -> tuple:  
    """ Функция находит числа с указанной разрядностью, сумма цифр которого равна 
    заданному значению.  
  
    :param digits: Разрядность чисел, <class 'int'>.
	:param sum_of_digits: Сумма цифр числа, <class 'int'>.
	:return: Кортеж из валидных чисел и количество валидных чисел,
	<class 'tuple'>.  
    """
	start = digits - 1  
    results = list()
      
    for value in range(10 ** start, 10 ** digits):  
        if sum(value // 10 ** exponent % 10 for exponent in range(start, -1, -1)) == sum_of_digits:  
            results.append(value)
	
    return results, len(results)
```

