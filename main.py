from item.item import Book,Item

# Book("three pigs", "child story", ["me", "antpu"]).save()

def show_menu():
    with open("config/main_menu.txt", "r") as menu:
        print("".join(menu.readlines()))
show_menu()
lib = Book.read_items()
opt = input("pls enter your option: ")
if opt == "1":
    for item in lib:
        print(item,lib[item])
elif opt == "6":
    while True:
        id_input = input("pls enter item id: ")
        res = Item.update_by_id(id_input)
        if res == id_input:
            break
        else:
            print(res)
elif opt == "7":
    while True:
        id_input = input("pls enter item id: ")
        res = Item.delete_by_id(id_input)
        if res == id_input:
            break
        else:
            print(res)