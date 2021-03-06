from getpass import getpass
from locale import currency
from data_objects.item import Article, Book, DigitalMedia,Item
from typing import Union
from data_objects.user import User
from services.borrow_return import BorrowReturnService
from util.constants import MAIN_MENU_URL, CHOOSE_TYPE_URL, BOOK_TYPE, DIGITAL_TYPE, ARTICLE_TYPE

'''
------------------------
    Library System
------------------------
 1.list all items
 2.list items by type
 3.borrow by id
 4.return by id
 5.add new item
 6.upadate by id
 7.delete by id
 q.quit
'''

# init data
item_db_all = Item.read_items()
users = User.read_users()
borrow_return_service = BorrowReturnService()

# print(users) #DEBUG

def show_ui(url):
    '''ui control'''
    with open(url, "r") as menu:
        print("".join(menu.readlines()))

def show_items(type:Union[str,None]=None):
    '''
    show items by type as argument
    by default type=none show all items
    '''
    if type == None:
        for item in item_db_all:
            print(item,item_db_all[item])
    else:
        for item in item_db_all:
            if item_db_all[item]["type"] == type:
                print(item,item_db_all[item])

def choose_type_op(book, art, digi):
    '''
    take functions as arguments
    callback according to diffrent choice
    ------------------------
    choose item type
    ------------------------
    1.Book
    2.Articles
    3.Digital Media
    q.quit to menu
    '''
    show_ui(CHOOSE_TYPE_URL)
    opt = input("pls enter your option: ")
    if opt == "1":
        book()
    elif opt == "2":
        art()
    elif opt == "3":
        digi()

def auth_user(uname,pwd) -> bool:
    if users[uname] == pwd:
        return True
    return False


username = input("pls enter username: ")
password = input("pls enter password: ") #DEBUG
# password = getpass("pls enter password: ")

if auth_user(username,password):
    print("login successful")
    while True:
        # ui and control logic
        show_ui(MAIN_MENU_URL)
        opt = input("pls enter your option: ")
        # list all items
        if opt == "1":
            show_items()
        # list items by type
        elif opt == "2":
            choose_type_op(
                lambda : show_items(BOOK_TYPE),
                lambda : show_items(ARTICLE_TYPE),
                lambda : show_items(DIGITAL_TYPE)
            )
        # 3.borrow by id
        elif opt == "3":
            id = input("pls enter item id: ")
            print("id: " + id + " processing...")
            borrow_return_service.log_borrow(username,id,item_db_all)
        # 4.return by id
        elif opt == "4":
            id = input("pls enter item id: ")
            print("id: " + id + " processing...")
            borrow_return_service.log_return(username,id)
        # 5.add new item
        elif opt == "5":
            def add_book():
                n = input("pls enter name: ")
                d = input("pls enter desciption:")
                a = input("pls enter authors, split by comma:")
                authors = a.split(',')
                Book(n,d,authors).save()
            def add_article():
                n = input("pls enter name: ")
                d = input("pls enter desciption:")
                Article(n,d).save()
            def add_digital_media():
                n = input("pls enter name: ")
                d = input("pls enter desciption:")
                DigitalMedia(n,d).save()
            choose_type_op(add_book, add_article, add_digital_media)
        #  6.upadate by id
        elif opt == "6":
            while True:
                id_input = input("pls enter item id: ")
                res = Item.update_by_id(id_input,item_db_all)
                if res == id_input:
                    break
                else:
                    print(res)
        #  7.delete by id
        elif opt == "7":
            while True:
                id_input = input("pls enter item id: ")
                if id_input in item_db_all:
                    print("curr:: " + "id: " + id_input + ", name: " + item_db_all[id_input]["name"] )
                    opt = input("delete? y/n: ")
                    if opt.lower() == "y":
                        if item_db_all[id_input]["type"] == BOOK_TYPE:
                            # cascade deleting associated data
                            Book.delete_by_id(id_input)
                    Item.delete_by_id(id_input,item_db_all)
                    break
                else:
                    print("invalid id")
        elif opt == "q":
            break
else:
    print("wrong username or password")