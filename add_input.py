username = input('Имя пользователя(ФИО): ')   # - имя пользователя
parts = username.split()
last_name = parts[0]
name = parts[1]
surname = parts[2]
initials = last_name +' '+ name[0]+'.'+ surname[0]+'.'
#print(initials)
title = input('Заголовок заметки: ')    # - заголовок заметки
content = input('Описание заметки: ')    # - описание заметки
status = input('Статус заметки: ')        # - статус заметки
created_date = input('Дата создания заметки(ДД.ММ.ГГГГ) ')    # - дата создания заметки в формате "день-месяц-год", например "10-11-2024"
issue_date = input('Дата истечения заметки(ДД.ММ.ГГГГ): ')     # - дата истечения заметки (дедлайн) в формате "день-месяц-год", например "10-12-2024"

temp_created_date = created_date[:6]+created_date[8:]
temp_issue_date = issue_date[:6]+issue_date[8:]

print('--------------------------------------------------')

print('Имя пользователя:', initials)
print('Заголовок заметки:',title)
print('Описание заметки:',content )
print('Статус заметки:',status)
print('Дата создания заметки:',temp_created_date)
print('Дата истечения заметки:',temp_issue_date)
