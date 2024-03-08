import json
import os


class TodoList:
    DIR_PATH = os.path.dirname(os.path.realpath(__file__))
    FILE_PATH = DIR_PATH+r"\todo_list.json"

    @staticmethod
    def initiate_file():
        with open(TodoList.FILE_PATH, "w") as file:
            json.dump({}, file, indent=4)

    @staticmethod
    def get_input():
        n = -1
        while type(n) != int or (n < 0 or n > 5):
            try:
                n = int(
                    input(
                        '''\nPress 1 To Display All Todo\
                        \nPress 2 To Add Todo\
                        \nPress 3 To Remove Todo\
                        \nPress 4 To Update Todo Value\
                        \nPress 5 To Update Todo Mark\
                        \nPress 0 To Exit\
                        \nEnter Input: '''
                    )
                )
            except:
                print("Wrong Input!! Kindly Enter Correct Input...")
        return n

    @staticmethod
    def read_file():
        if not os.path.isfile(TodoList.FILE_PATH):
            TodoList.initiate_file()
        data = {}
        try:
            with open(TodoList.FILE_PATH, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{TodoList.FILE_PATH}' not found.")
        except json.JSONDecodeError:
            print(
                f"Error: Unable to decode JSON from file '{TodoList.FILE_PATH}'.")
        finally:
            return data

    def write_file(data):
        with open(TodoList.FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)

    def display_todo():
        unchecked = "\u2610"
        checked = "\u2611"
        data = TodoList.read_file()
        if not len(data):
            print("No Todos Present\n")
        for key, value in data.items():
            content = value.get("Content", None)
            mark = checked if value.get("Mark", None) else unchecked
            print(f"{key}- {mark} {content}")

    def add_todo():
        value = input("\nEnter Todo: ")
        data = TodoList.read_file()
        key = str(int(sorted(data)[-1])+1) if len(data) > 0 else "1"
        data.update({key: {"Content": value, "Mark": False}})
        TodoList.write_file(data)

    def remove_todo():
        key = input("Enter Todo Id To Remove: ")
        try:
            key = int(key)
            data = TodoList.read_file()
            if str(key) in data:
                del data[str(key)]
                TodoList.write_file(data)
                print(F"Todo with id {key} removed")
            else:
                print(F"Todo with ID {key} is not present in List")
        except:
            print("Wrong Input")

    def update_todo_value():
        key = input("Enter Todo Id To Update Value: ")
        try:
            data = TodoList.read_file()
            if key in data:
                value = input("Enter Todo Value: ")
                data[key]["Content"] = value
                TodoList.write_file(data)
                print(F"Todo Value with id {key} Updated")
            else:
                print(F"Todo with ID {key} is not present in List")
        except:
            print("Wrong Input")

    def update_todo_mark():
        key = input("Enter Todo Id To Update Mark: ")
        try:
            data = TodoList.read_file()
            if key in data:
                data[key]["Mark"] = not data[key]["Mark"]
                TodoList.write_file(data)
                print(F"Todo Mark with id {key} Updated")
            else:
                print(F"Todo with ID {key} is not present in List")
        except:
            print("Wrong Input")
