# ● At least the following classes: Library, Items, Books, Articles, Digital Media, Members
# ● Books, Articles, Digital Media should be a subclass of Items.
# ● Each class should have an __init__ and __str__ methods. 
# library.txt,items.txt, members.txt, and borrowing.txt 

import csv
from util.constants import ITEMS_FILE_URL,BOOK_AUTHOR_FILE_URL,BOOK_TYPE


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
        '''
        return dict using id as key, filtered by type.
        '''
        db = {}
        try:
            with open(ITEMS_FILE_URL, "r", newline="") as items_file:
                reader = csv.DictReader(items_file)
                for item in reader:
                    # if type != None, then filter by type
                    if( (type == None) or (type == item["type"]) ):
                        # add new element using id as key 
                        db[item.get("id")] = {}
                        # package all k,v pairs other than id into dict into new element 
                        for key in item:
                            if key != "id":
                                db[item.get("id")][key] = item.get(key)
        except:
            # print("file items.csv doesn't exist") # DEBUG
            pass
        return db

    def save(self) -> str:
        '''
        save item into file, return id of the item
        '''
        headers = ["id", "name", "type", "description"]
        # initial value of id is 0
        id = 0
        try:
            db = Item.read_items()
            # file doesn't exist or empty file go to except block
            if db == {}:
                raise IOError
            # file is not empty then add new line to the end of the file
            with open(ITEMS_FILE_URL, "a", newline="") as items_file:
                writer = csv.DictWriter(items_file, headers)
                # find largest id
                for key_id in db:
                    if(int(key_id)>id):
                        id = int(key_id)
                # increment by 1 to get new id
                id += 1
                writer.writerow({"id": str(id), "name": self.name, "type": self.type, "description": self.description })
        except IOError:
            # empty file write from start
            with open(ITEMS_FILE_URL, "w", newline="") as items_file:
                writer = csv.DictWriter(items_file, headers)
                writer.writeheader()
                writer.writerow({"id": str(id), "name": self.name, "type": self.type, "description": self.description })
        return id

    def save_db_item(db:dict[str,dict]):
        '''
        take modified db returned by read_items() and save to file
        '''
        headers = ["id", "name", "type", "description"]
        with open(ITEMS_FILE_URL, "w", newline="") as items_file:
            writer = csv.DictWriter(items_file, headers)
            writer.writeheader()
            for key_id in db:
                writer.writerow({"id": key_id, "name": db[key_id]["name"], "type": db[key_id]["type"], "description": db[key_id]["description"] })
        print("<saved>")
    
    def update_by_id(id:str) -> str:
        '''
        update by id
        return same id for successful operation
        return error message for invalid id 
        '''
        # read db from file
        db = Item.read_items()
        if id in db:
            print("curr:: " + "id: " + id + ", name: " + db[id]["name"] )
            while True:
                opt = input("pls enter the option (name/description/save/q): ")
                if opt == "save":
                    # write back changed db to file
                    Item.save_db_item(db)
                    break
                elif opt == "name" or opt == "description":
                    value = input("pls enter new value: ")
                    # save change to db
                    db[id][opt] = value
                    print("change staged:" + opt + ":" + value)
                elif opt == "q":
                    print("<canceled>")
                    break
                else:
                    print("invalid option")

            return id
        else:
            return "invalid id"
    
    def delete_by_id(id:str):
        '''
        delete by id
        return same id for successful operation
        return error message for invalid id 
        '''
        db = Item.read_items()
        if id in db:
            print("curr:: " + "id: " + id + ", name: " + db[id]["name"] )
            opt = input("delete? y/n: ")
            if opt.lower() == "y":
                if db[id]["type"] == BOOK_TYPE:
                    book_author_db = Book.read_book_author()
                    del book_author_db[id]
                    Book.save_db_book_author(book_author_db)
                del db[id]
                Item.save_db_item(db)
            return id
        else:
            return "invalid id"
        


# book class inherit item class
class Book(Item):

    def __init__(self, name:str, description:str, authors:list[str] ) -> None:
        Item.__init__(self, name, BOOK_TYPE, description)
        self.authors = authors

    def __str__(self) -> str:
        return Item.__str__(self) + ", authors: " + ", ".join(self.authors)

    def read_items() -> dict[str, dict]:
        '''
        get all items of type Book
        '''
        return Item.read_items(type=BOOK_TYPE)

    def read_book_author() -> dict[str,list[str]]:
        '''
        get book_author file to k:id, v:author list
        '''
        db = {}
        with open(BOOK_AUTHOR_FILE_URL, "r", newline="") as book_author_file:
            reader = csv.DictReader(book_author_file)
            for item in reader:
                if item["id"] in db:
                    db[item["id"]].append(item["author"])
                else:
                    db[item["id"]] = [item["author"]]
        return db

    def save_db_book_author(db: dict):
        headers = ["id", "author"]
        with open(BOOK_AUTHOR_FILE_URL, "w", newline="") as book_author_file:
            writer = csv.DictWriter(book_author_file, headers)
            writer.writeheader()
            for id in db: 
                for author in db[id]:
                    writer.writerow({"id": id, "author": author })


    def save(self) -> str:
        '''
        save item of type "book"
        '''
        # save general info to items file
        id = Item.save(self)
        # save author info to book_author file
        headers = ["id", "author"]
        try:
            db = Book.read_book_author()
            # if file no existance or empty go to except block
            if len(db) == 0:
                raise IOError
            # save using the same id used for items file
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
    
    def delete_by_id(id: str):
        return super().delete_by_id()
