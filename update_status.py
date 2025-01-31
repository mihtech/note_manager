note = []

username = input('Введите ваше имя: ') # имя пользователя

titles = []
while True: # цикл для ввода заголовка
    user_input = input('Введите заголовок (или оставьте пустым для завершения):')
    if user_input == '': # проверка на пустой ввод
        break # завершение цикла
    else:
        if user_input in titles: # проверка на дубликаты
            print(f'Заголовок: "{user_input}" уже существует')
        elif user_input.isspace() == True: # проверка на имена состоящие только из пробелов и табуляции
            print('Заголовок не может состоять только из пробелов и табуляции')
        else:
            titles.append(user_input) # добавление заголовка

content = input('Введите описание заметки: ') # описание заметки

created_date = input('Введите дату создания заметки(дд-мм-гггг): ') # дата создания заметки в формате "день-месяц-год", например "10-11-2024"

issue_date = input('Введите дату истечения заметки(дд-мм-гггг): ') # дата истечения заметки (дедлайн) в формате "день-месяц-год", например "10-12-2024"

status = []
while True:
    status = 'активна'
    user_input = input(f'Текущий статус заметки: "{status}", изменить статус? Да(y)/Нет(n): ') # статус заметки
    if user_input.lower() == 'y' or user_input.lower() == 'да' or user_input.lower() == 'yes':
        if status == 'активна':
            status = 'не активна'
            break
        elif status == 'не активна':
            status = 'активна'
            break
    if user_input.lower() == 'n' or user_input.lower() == 'нет' or user_input.lower() == 'no':
        break
    else:
        print('Не верный ввод')

note = [
    username,
    titles,
    content,
    status,
    created_date,
    issue_date
]

count = (len(note[1]))
i = 1

print(f'Имя пользователя:  {note[0]} ')
if i <= count:
    for title in titles:
        print(f'Заголовок {i}: {note[1][i - 1]}') # вывод списка заголовков
        i += 1

print(f'Описание заметки:  {note[2]} ')
print(f'Статус заметки:  {note[3]} ')
print(f'Дата создания заметки:  {note[4]} ')
print(f'Дата истечения заметки (дедлайн):  {note[5]} ')
