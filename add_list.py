# Создаем пустой список для заголовков
title = []

# Запрашиваем у пользователя три заголовка
title1 = input("Введите первый заголовок: ")
title2 = input("Введите второй заголовок: ")
title3 = input("Введите третий заголовок: ")

# Добавляем заголовки в список
title.append(title1)
title.append(title2)
title.append(title3)

# Выводим все заголовки
for titles in title:
    print(titles, end=', ')

print(end='\n---------------------\n')

# Создаем пустой список для заголовков
title = []

# Запрашиваем у пользователя три заголовка
title1 = input("Введите первый заголовок: ")
title2 = input("Введите второй заголовок: ")
title3 = input("Введите третий заголовок: ")

# Добавляем заголовки в список
title.extend([title1 , title2 , title3])


# Выводим все заголовки

for titles in title:
    print(titles, end=', ')

print(end='\n---------------------\n')

title1 = input("Введите первый заголовок: ")
title2 = input("Введите второй заголовок: ")
title3 = input("Введите третий заголовок: ")
title = [title1 , title2 , title3]

for titles in title:
           print(titles,end=', ')

print(end='\n---------------------\n')
