todo_list = []

def add_task(task):
    todo_list.append(task)

def remove_task(task):
    todo_list.remove(task)

def show_tasks():
    for index, task in enumerate(todo_list, 1):
        print(f"{index}. {task}")
def save_tasks():
    with open('tasks.txt', 'w', encoding='utf-8') as f:
        for task in todo_list:
            f.write(task + '\n')
def load_tasks():
    try:
        with open('tasks.txt', 'r', encoding='utf-8') as f:
            for line in f:
                todo_list.append(line.strip())
    except FileNotFoundError:
        pass
load_tasks()
while True:
    print("=== Todo List ===")
    print("1. Добавить задачу")
    print("2. Удалить задачу")
    print("3. Показать задачи")
    print("4. Выйти")

    choice = input("Выбери действие: ")

    if choice == "1":
        print("ты выбрал добавить")
        add_task(input('Введи задачу:'))
        save_tasks()
    elif choice == '2':
        print('ты выбрал удалить')
        if len(todo_list) == 0:
            print('список пуст!')
        else:
            show_tasks()
            try:
                number = int(input('Введи номер: '))
                task = todo_list[number - 1]
                remove_task(task)
                save_tasks()
            except ValueError:
                print('такой задачи нет в списке!')
            except IndexError:
                print('нет такой цифры')
    elif choice == '3':
        print('список задач:')
        show_tasks()
    elif choice == '4':
        save_tasks()
        break
    else:
        print('нет такого действия')

