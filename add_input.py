username = input('Введите ваше имя: ') # имя пользователя
title = input('Введите заголовок заметки:' ) # заголовок заметки
content = input('Введите описание заметки: ') # описание заметки
status = input('Введите статус заметки (например, "активна", "завершена"): ') # статус заметки
created_date = input('Введите дату создания заметки(дд-мм-гггг): ') # дата создания заметки в формате "день-месяц-год", например "10-11-2024"
issue_date = input('Введите дату истечения заметки(дд-мм-гггг): ') # дата истечения заметки (дедлайн) в формате "день-месяц-год", например "10-12-2024"

print('имя пользователя:', username)
print('заголовок заметки:', title)
print('описание заметки:', content)
print('статус заметки:', status)
print('дата создания заметки:', created_date)
print('дата истечения заметки (дедлайн):', issue_date)
print('дата создания заметки для пользователя:', created_date[0:5])
print('дата истечения заметки (дедлайн) для пользователя:', issue_date[0:5])