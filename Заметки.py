head = "Простые Заметки"
print(f"{head:.^30}")
def show_menu():
    print("\n1) Показать все заметки\n2) Добавить заметку\n3) Очистить все заметки\n4) Выйти\n5) Показать меню\n")
show_menu()
while True:
    try:
        choice = int(input(""))
        
        if choice == 1:
            with open("notes.txt", "r", encoding="utf-8") as file:
                content = file.read()
                if content == "":
                    print("Заметки не найдены\n")
                else:
                    print(content)
        elif choice == 2:
            with open("notes.txt", "a", encoding="utf-8") as file:
                new_zam = input("Напишите новую заметку\n")
                file.write(new_zam + "\n")
                print("Заметка добавлена!\n")
        elif choice == 3:
            with open("notes.txt", "w", encoding="utf-8") as file:
                file.write("")
                print("Заметки удалены!\n")
        elif choice == 4:
            break
        elif choice == 5:
            show_menu()
        else:
            print("Неизвестная ошибка\n")

    except FileNotFoundError:
        print("Заметки не найдены\n")
    except ValueError:
        print("Выберите одно из списка\n")
    except:
        print("Неизвестная ошибка\n")