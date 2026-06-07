import json
import os
import datetime 


# Сохранить задачи в файл
def save_tasks():
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)


# Вывод задач
def show_tasks():
    s = ""
    for k in tasks:
        s += f"{k}\n"
    return s


# Добавить задачу
def add_task(task, ctg, prior):
    if task.strip() == "":
        print("Задача не указана. Попробуйте заново.")
        return
    else:
        date = datetime.date.today()
        tasks.append(
            {
                "id": len(tasks) + 1,
                "ЗАДАЧА": task,
                "STATUS": "Не выполнена",
                "Category": ctg,
                "Priority": prior,
                'Date': date.isoformat()
            }
        )
        print("Задача добавлена")
        save_tasks()
        return tasks


# Удалить задачу
def del_task(rmv_tsk):
    try:
        rmv_tsk = int(rmv_tsk)
        if 1 <= rmv_tsk <= len(tasks):
            del tasks[rmv_tsk - 1]
            print("Задача успешно удалена")
        else:
            print("Задачи под таким номером не существует")
    except ValueError:
        print('Некорректный ввод данных')
    save_tasks()


# Изменить статус задачи
def complete_task(check):
    try:
        check = int(check)
        if 0 < check > len(tasks):
            print("Ошибка. Не совпадают номера задач.")
        elif tasks[check - 1]["STATUS"] == "Выполнено":
            print("Задача уже выполнена.")
        else:
            tasks[check - 1]["STATUS"] = "Выполнено"
            print("Задача выполнена!")
    except ValueError:
        print('Некорректный ввод данных')
    save_tasks()
    return tasks


# Изменить задачу
def change_tasks(id):    # вот тут id обработать в Int 
    try:
        id = int(id)
        tasks[id - 1]["ЗАДАЧА"] = input("Введите новую задачу: ")
    except ValueError:
        print('Некорректный ввод данных')
    except IndexError:
        print('Некорректный ввод данных')

# Загрузить из файла данные
def load_json_file():
    if os.path.exists("tasks.json") and os.path.getsize("tasks.json") > 0:  # Проверка на наличие файла и его размер
        with open("tasks.json", "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []


# Поиск задачи по тексту
def find_task(s):
    found = False
    for i in tasks:
        if s in i["ЗАДАЧА"]:
            print(i)
            found = True
    if not found:
        print("Задача не найдена. Проверьте правильность написания текста.")


# Фильтрация вывода
def sort_task(n):
    try:
        n = int(n)
        if n == 1:
            print(*tasks)
        elif n == 2:
            for i in tasks:
                if i["STATUS"] == "Выполнено":
                    print(i)
        elif n == 3:
            for k in tasks:
                if k["STATUS"] != "Выполнено":
                    print(k)
        else:
            print("Не правильный ввод опции")
    except ValueError:
        print('Некорректный ввод данных')


# Удаление выполненных задач
def del_complete_tasks():
    global tasks
    new_tasks = []
    for i in range(len(tasks)):
        if tasks[i]["STATUS"] != "Выполнено":
            new_tasks.append(tasks[i])
    tasks = new_tasks
    print('Выполненные задачи успешно удалены.')
    save_tasks()

check_complete = "Не выполнена"

tasks = load_json_file()

print("=== Менеджер задач ===\n1. Показать задачи\n2. Добавить задачу\n3. Редактировать задачу\n4. Изменить статус задачи\n5. Удалить задачу\n6. Найти задачу\n7. Фильтровать задачи\n8. Удалить все выполненные\n9. Выйти\n")
user_input = input("Выберите  задачу: ")


while user_input != "9":  
    # Показать задачи
    if user_input == "1":
        if tasks == []:
            print("Задач нет")
        else:
            print(show_tasks())
    # Добавить задачу
    elif user_input == "2":
        add_task(input("Введите задачу: "), input("И ее категорию: "), input('Введите также приоритет задачи (Низкий, Средний, Высокий): '))

    # Редактирование задач
    elif user_input == "3":
        if tasks != []:
            print(f"Список задач: \n{show_tasks()}")
            change_tasks(input("Введите номер задачи, которую хотите изменить: "))
        else:
            print("Задач пока нет.")

    # Изменить статус задачи
    elif user_input == "4":
        if tasks != []:
            print(f"Список задач: \n{show_tasks()}")
            complete_task(input("Введите номер задачи которую хотите решить.\n"))

        else:
            print("Задач пока нет.")

    # Удаление задачи
    elif user_input == "5":
        if tasks != []:
            print(f"Список задач: \n{show_tasks()}")
            del_task(input("Введите задачу, которую хотите удалить.\n"))
        else:
            print("Задач пока нет.")
    # Поиск задачи по тексту
    elif user_input == "6":
        if tasks != []:
            find_task(input("Введите текст задачи, которую хотите найти:\n"))

    # Фильтрация вывода
    elif user_input == "7":
        if tasks != []:
            sort_task(
                input(
                    "1. Показать все задачи \n2. Показать выполненные задачи \n3. Показать невыполненные задачи\nВведите номер опции:\n"
                )
            )
        else:
            print("Задач пока нет")
    # Удаление выполненных задач
    elif user_input == "8":
        if tasks != []:
            del_complete_tasks()

    else:
        print("Не соответствие номера задачи")

    user_input = input("Выберите  задачу: ")

print("Завершение работы") 