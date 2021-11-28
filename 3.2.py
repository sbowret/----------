dic = {}
what = input("Добавить ли задачу:")
if what == "Да" "да" "Yes" "yes" "1":
    while True:
        dic.update({input("Введите дату:") : input("Введите задачу:")})
        what = input("Добавить ещё задачу:")
        if what == "Нет":
            break
elif what == "Нет" "0":
    print("пока")
else:
    print("Команда не найдена")
print(dic)
