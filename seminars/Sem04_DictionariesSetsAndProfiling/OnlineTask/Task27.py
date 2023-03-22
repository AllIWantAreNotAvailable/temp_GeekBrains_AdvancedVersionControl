""" Задача №27:
Пользователь вводит текст(строка). Словом считается последовательность непробельных символов
идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных
слов содержится в этом тексте.

Input:
- She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she
 sells sea shells on the sea shore I'm sure that the shells are sea shore shells
Output:
- 13
"""


source_string = "She sells sea shells on the sea shore\n" \
                "The shells that she sells are sea shells I'm sure\n" \
                "So if she sells sea shells on the sea shore\n" \
                "I'm sure that the shells are sea shore shells"

no_repeat = set(map(lambda el: el.lower(), source_string.split()))
print(source_string, end='\n\n')
print(', '.join(map(lambda el: f'"{el}"', no_repeat)), len(no_repeat), sep='\nВсего, слов -> ')
