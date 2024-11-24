# Создаем пустой список для заголовков
titles = []

# Запрашиваем у пользователя три заголовка
title1 = input("Введите первый заголовок: ")
title2 = input("Введите второй заголовок: ")
title3 = input("Введите третий заголовок: ")

# Добавляем заголовки в список
titles.append(title1)
titles.append(title2)
titles.append(title3)

# Выводим все заголовки
print("Заголовки заметки:")
for title in titles:
    print(title)
