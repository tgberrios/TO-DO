class TodoList:
    def __init__(self):
        self.data_file = open(r"C:\Users\TomyGustavo\OneDrive - MSFT\PROYECTOS\PROJECTS\TO-DO\data.txt", "a+")

    def add(self, task):
        self.data_file.write(task + '\n')
        self.data_file.flush()

    def rem(self):
        self.data_file.seek(0)  # Reset file pointer to the beginning
        tasks = self.data_file.readlines()
        if not tasks:
            print("No hay tareas para eliminar.")
            return
        print("Lista de tareas:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")
        print("¿Qué elemento deseas eliminar?")
        index = int(input())
        if index < 1 or index > len(tasks):
            print("El índice dado está fuera del rango.")
            return
        self.data_file.seek(0)
        self.data_file.truncate()
        del tasks[index - 1]
        for task in tasks:
            self.data_file.write(task)
        print("Elemento eliminado correctamente.")

    def tasks(self):
        self.data_file.seek(0)  # Reset file pointer to the beginning
        tasks = self.data_file.readlines()
        if not tasks:
            print("No hay tareas.")
        else:
            for i, task in enumerate(tasks, 1):
                task = task.strip()
                print(f"{i}. {task}")

def main():
    todo_List = TodoList()

    while True:
        print("\n1. Add")
        print("2. Rem")
        print("3. View")
        print("4. Exit")

        choice = input("Seleccione una opcion: ")

        if choice == "1":
            task = input("Ingresa la tarea: ")
            todo_List.add(task)

        elif choice == "2":
            todo_List.rem()

        elif choice == "3":
            todo_List.tasks()

        elif choice == "4":
            todo_List.data_file.close()
            break

        else:
            print("Opcion no valida!")

if __name__ == "__main__":
    main()
