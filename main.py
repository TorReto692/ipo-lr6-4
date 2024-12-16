podstr = input("Введите строку для поиска: ") #Запрос строки от пользователя

with open('text.txt', 'r', encoding='utf-8') as file: #Открываем файл в режиме чтения 
    strk = file.readlines() #Считывание строк
    
lines = [] #Создание списка

for line in strk: #Цикл
    if podstr in line: #Проверка подстроки 
        lines.append(line) #Добавление строк в список без пробелов 
        
lenLines = len(lines) #Количество найденых строк
print("Количество строк с подстрокой: {}".format(lenLines)) #Вывод на экран

for line in lines: #Цикл
    print(line) #Вывод на экран
    
sorted_lines = sorted(lines, key = len) #Сортируем список по длине строк

for line in sorted_lines: #Цикл отсортированных строк
    print(f"Сортированные строки: {line}") #Вывод на экран
    