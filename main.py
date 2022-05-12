# ● At least the following classes: Library, Items, Books, Articles, Digital Media, Members
# ● Books, Articles, Digital Media should be a subclass of Items.
# ● Each class should have an __init__ and __str__ methods. 
# library.txt,items.txt, members.txt, and borrowing.txt 

import csv
import uuid

ITEMS_FILE_URL = "items.csv"
BOOK_AUTHOR_FILE_URL = "book_author.csv"

# item class
class Item:

    def __init__(self, name:str, type:str, description:str) -> None:
        self.name = name
        self.type = type
        self.description = description

    def __str__(self) -> str:
        return "name: " + self.name + ", type: " + self.type + ", description: " + self.description

    def read_headers() -> list[str]:
        with open(ITEMS_FILE_URL, "r", newline="") as items_file:
            headers = items_file.readline().split(",")
            return headers

    def read_items(type=None) -> dict[str, dict]:
        db = {}
        with open(ITEMS_FILE_URL, "r", newline="") as items_file:
            reader = csv.DictReader(items_file)
            for item in reader:
                if( (type == None) or (type == item["type"]) ):
                    db[item.get("id")] = {}
                    for key in item:
                        if key != "id":
                            db[item.get("id")][key] = item.get(key)
        return db

    def save(self) -> str:
        headers = ["id", "name", "type", "description"]
        id = uuid.uuid4()
        try:
            db = Item.read_items()
            if db == {}:
                raise IOError
            with open(ITEMS_FILE_URL, "a", newline="") as items_file:
                writer = csv.DictWriter(items_file, headers)
                while id in db:
                    id = uuid.uuid4()
                writer.writerow({"id": id, "name": self.name, "type": self.type, "description": self.description })
        except IOError:
            with open(ITEMS_FILE_URL, "w", newline="") as items_file:
                writer = csv.DictWriter(items_file, headers)
                writer.writeheader()
                writer.writerow({"id": id, "name": self.name, "type": self.type, "description": self.description })
        return id


# book class
class Book(Item):

    def __init__(self, name:str, description:str, authors:list[str] ) -> None:
        Item.__init__(self, name, "Book", description)
        self.authors = authors

    def __str__(self) -> str:
        return Item.__str__(self) + ", authors: " + ", ".join(self.authors)

    def read_book_author() -> set[tuple]:
        pk_set = set()
        with open(BOOK_AUTHOR_FILE_URL, "r", newline="") as book_author_file:
            reader = csv.DictReader(book_author_file)
            for item in reader:
                pk = (item["id"], item["author"])
                pk_set.add(pk)
        return pk_set

    def save(self) -> str:
        id = Item.save(self)
        headers = ["id", "author"]
        try:
            pk_set = Book.read_book_author()
            if len(pk_set) == 0:
                raise IOError
            with open(BOOK_AUTHOR_FILE_URL, "a", newline="") as book_author_file:
                writer = csv.DictWriter(book_author_file, headers)
                for author in self.authors:
                    writer.writerow({"id": id, "author": author })
        except IOError:
            with open(BOOK_AUTHOR_FILE_URL, "w", newline="") as book_author_file:
                writer = csv.DictWriter(book_author_file, headers)
                writer.writeheader()
                for author in self.authors:
                    writer.writerow({"id": id, "author": author })
        return id


# Book("three pigs", "child story", ["me", "antpu"]).save()

def show_menu():
    with open("main_menu.txt", "r") as menu:
        print("".join(menu.readlines()))
show_menu()
lib = Item.read_items()
input = input("pls enter your option:")
if input == "1":
    for item in lib:
        print(item,lib[item])