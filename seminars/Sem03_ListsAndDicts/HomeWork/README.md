***Общие комментарии по выполнению самостоятельной работы:***
> Возможно, работа выполнена с забеганием вперед, использованы не рассмотренные на текущем этапе структуры и методы, прошу простить за "торопыжничество". В ходе выполнения работы: поставленные задачи декомпозированы на методы (без фанатизма), основная логика запускается из точки входа и расположена в методе main(). Обработан ввод пользователя там, где того требует подход к решению. К вынесенным из main() написана исчерпывающая документация.

> PS: Гиперссылки на соответсвующее директории репозитория GitHub привязаны к наименованиям маркеров вида **"Задача №*"**

> ***PSS:*** Буду рад оставленным комментариям и замечаниям по представленным решениям.

- [**Задача №16**](https://github.com/AllIWantIsNotAvailable/GeekBrains_IntroductionToPython/blob/main/seminars/Sem03_ListsAndDicts/HomeWork/Task16.py):

Комментарии к задаче:
> Условие скорректировано на семинаре, задается неупорядоченный список и заполняется случайными значениями.
> Ввод пользователя вынесен в отдельный метод с обработкой исключений. В случае исключительной ситуации, вызывается рекуррентный случай метода. 
> Основная логика решения вынесена в отдельный метод:

```Python
def get_count_value_in_list(list_of_values: list, value) -> int:
	""" Считает, сколько раз значение (value) встретилось в списке
	(list_of_values).
	
	:param list_of_values: Список со значениями, <class 'list'>.
	:param value: Искомое значение, <class 'int'>.
	:return: Сколько раз значение встретилось в списке, <class 'int'>.	
	"""

	return list_of_values.count(value)
```


- [**Задача №18**](https://github.com/AllIWantIsNotAvailable/GeekBrains_IntroductionToPython/blob/main/seminars/Sem03_ListsAndDicts/HomeWork/Task18.py):

Комментарии к задаче:
> Условие скорректировано на семинаре, задается неупорядоченный список и заполняется случайными значениями.
> Ввод пользователя вынесен в отдельный метод с обработкой исключений. В случае исключительной ситуации, вызывается рекуррентный случай метода. 
> Основная логика решения вынесена в отдельный метод:

```Python
def get_value_close_to_desired(list_of_values: list, looking_for: int) -> tuple:
	""" Возвращает значения наиболее близкое или равное переданному
	(searching_value) из списка (list_of_values).
	
	:param list_of_values: Список значений, в котором ведется поиск,
	<class 'list'>.
	:param looking_for: Значение, которое ищем в списке, <class 'list'>.
	:return: Значения наиболее близкое к искомому, <class 'tuple'>.
	"""
	
	sorted_values = sorted(list_of_values)
	lower = sorted_values[0]
	bigger = sorted_values[-1]
	
	
	if looking_for <= lower:
		return lower,
	elif bigger <= looking_for:
		return bigger,
	
	for index in range(1, len(sorted_values[1:])):
		current = sorted_values[index]
	
		if current == looking_for:
			return current,
		elif current < looking_for:
		continue
	
		previous = sorted_values[index - 1]
	
		if abs(previous - looking_for) < abs(current - looking_for):
			return previous,
		elif abs(previous - looking_for) == abs(current - looking_for):
			return previous, current
		else:
			return current,
```

- [**Задача №20**](https://github.com/AllIWantIsNotAvailable/GeekBrains_IntroductionToPython/blob/main/seminars/Sem03_ListsAndDicts/HomeWork/Task20.py):

Комментарии к задаче:
> Основная логика решения вынесена в отдельный метод:

```Python
def main() -> None:
	""" Главная функция
	
	:return: None
	"""

	user_strint = input('Введите слово:\n>>> ')
	table_of_values = get_table_of_values() # Словарь из условия
	
	result = 0
	for char in user_strint:
		result += table_of_values[char.upper()]
	print(f'За слово "{user_strint}" вы заработали {result} очков.')
```

- [**Задача со звёздочкой №2**](https://github.com/AllIWantIsNotAvailable/GeekBrains_IntroductionToPython/blob/main/seminars/Sem03_ListsAndDicts/HomeWork/TaskStar02.py):

Комментарии к задаче:
> Основная логика решения вынесена в отдельный метод:

```Python
def is_anagram(first: str, second: str) -> bool:
	""" Проверяет утверждение: "Переданные строки являются анаграммами".
	
	Как работает:
		1. Преобразуем строки в списки и сортируем по алфавиту.
		2. Инициализируем флаг утверждением: "Длина списка1 равна длине списка2".
		3. Если утверждение п. 2 Истинно, тогда поэлементно сравниваем 
		отсортированные на п. 1 списки.
		4. Если очередная пара элементов не прошла проверку на равенство,
		инвертируем флаг в Ложь и прерываем цикл.
		5. Возвращаем значение флага.
	
	:param first: Первая строка для сравнения, <class 'str'>
	:param second: Вторая строка для сравнения, <class 'str'>
	:return: Истинность утверждения: "Переданные строки являются анаграммами";
	<class 'bool'>
	"""
	# Преобразуем в упорядоченный список
	first, second = str_to_list(first), str_to_list(second)
	first_length = len(first)
	flag = first_length == len(second)
	
	if flag:
		for index in range(first_length):
			if first[index].upper() != second[index].upper():
				flag = not flag
				break
	
	return flag
```

- [**Задача со звёздочкой №3**](https://github.com/AllIWantIsNotAvailable/GeekBrains_IntroductionToPython/blob/main/seminars/Sem03_ListsAndDicts/HomeWork/TaskStar03.py):

Комментарии к задаче:
> Основная логика решения вынесена в отдельный метод:

```Python
def query(**kwargs) -> str:
	""" Преобразуем переданный словарь в строку запроса, сформированную из отсортированных в лексикографическом порядке параметров.
	
	Подход к решению:
	- генерируем список кортежей из ключей и значений;
	- сортируем список по первому элементу кортежа ("ключу словаря");
	- генерируем список из отсортированного с форматированием элементов
	по ф-строке и сливаем все в строку с разделителем.
	
	:param kwargs: Словарь с параметрами, <class 'dict'>
	:return: Строка запроса, <class 'str'>
	"""

	key_value_list = [(key, value) for key, value in kwargs.items()]
	key_value_list.sort(key=lambda el: el[0])
	return '&'.join(f'{k}={v}' for k, v in key_value_list)
```
