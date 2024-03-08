from TodoList import TodoList


def todo_list():
    n = None
    while n != 0:
        n = TodoList.get_input()
        if n == 0:
            break
        if n == 1:
            TodoList.display_todo()
        elif n == 2:
            TodoList.add_todo()
        elif n == 3:
            TodoList.remove_todo()
        elif n == 4:
            TodoList.update_todo_value()
        elif n == 5:
            TodoList.update_todo_mark()


if __name__ == '__main__':
    todo_list()
