def show_tasks():
    if tasks == []:
        print("Задач нет")
    else:
        print(*tasks)


def add_task(task):
    if task.strip == None:
        print("Задача не указана. Попробуйте заново.")
    else:
        tasks.append({'id': len(tasks) + 1, 'ЗАДАЧА': task, 'STATUS': "He выполнена"})
    print('Задача добавлена')
    return tasks
    

def del_task(rmv_tsk):
    del tasks[int(rmv_tsk) - 1]


def complete_task():
    check = input('Введите номер задачи которую хотите решить.\n')
    if int(check) >= len(tasks):
        print('Ошибка. Не совпадают номера задач.')
    elif tasks[int(check)]['STATUS'] == "Выполнено":
        print("Задача уже выполнена.")
    else:
        tasks[int(check)]['STATUS'] = "Выполнено"
    return tasks


check_complete = "He выполнена"
start = "=== Менеджер задач ===\n1. Показать задачи\n2. Добавить задачу\n3. Удалить задачу\n4. Завершить задачу\n5. Выйти\n"
tasks = []

print(start)
user_input = input("Выберите  задачу: ")


while user_input != "5":
    if user_input == "1":
        show_tasks()
    elif user_input == "2":
        add_task(input("Введите задачу: "))
    elif user_input == "3":
        if tasks != []:
            print(f"Список задач: {tasks}")
            del_task(input("Введите номер задачи, которую хотите удалить: "))
        else:
            print("Задач пока нет.")
    elif user_input == '4':
        if tasks != []:
            print(f"Список задач: \n{tasks}")
            complete_task()
        else:
            print("Задач пока нет.")
    else:
        print('Не соответсвие номера задачи')

    user_input = input("Выберите  задачу: ")

print("Завершение работы")
