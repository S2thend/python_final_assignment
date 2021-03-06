# python_CA
LIBRARY MANAGEMENT SYSTEM:
You are asked to develop an application to manage library services, such as borrowing and
returns activities. You should be able to borrow/return a book, an article in a journal, or
digital media. All the library information should be stored in four external files:
library.txt, items.txt, members.txt, and borrowing.txt. It is up to you to define
the structure of each file, but each member, item or transaction should have an unique ID.
Use Python classes to implement the library. Some of the functionality your system should
provide includes:
● At least the following classes: Library, Items, Books, Articles, Digital Media, Members
● Books, Articles, Digital Media should be a subclass of Items.
● Each class should have an __init__ and __str__ methods. For each __str__ method,
think what information each class should provide when you print their instances.
● Persistent memory: when you start your system it should read the files library.txt,
items.txt, members.txt, and borrowing.txt in the same folder as the python
code and create all the necessary instances.
● Provide a command line interface for the user to:
○ Add/edit/delete instances belonging to each class,
○ Members browse library items and select items to borrow.
○ Members returning borrowed items.
○ Make sure to update the external files after any information is modified
# project structure
```
src
│  .gitignore
│  main.py
│  README.md
│  test_install.py
│  __init__.py
│
├─config
│      main_menu.txt
│      type_choice.txt
│
├─database
│      book_author.csv
│      borrow_log.csv
│      items.csv
│      users.csv
│
├─data_objects
│     item.py
│     user.py
│
├─services
│     borrow_return.py
│   
│  
│
└─util
    constants.py
```
# difficulties
1. to make sure data consistency in associated diffrerent files
2. to decouple the functions nicely using oop, espeicaially where to keep all the data to make sure data consistency and least possibly access to data files
3. to split logics into classes and modules clearly, this projct is still underdeveloped and need refactoring

# User Manual 
## set up enviroment
run test_install.py to generate test data
this will generate two users
username:"user1",password:"123456"
username:"user2",password:"123456789"
use these to login

## ---console output examples---
## 2.list by type
```
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
pls enter your option: 2
------------------------
   choose item type
------------------------
 1.Book
 2.Articles
 3.Digital Media
 q.quit to menu
pls enter your option: 1
0 {'name': 'three pigs', 'type': 'Book', 'description': 'child story'}
1 {'name': 'three pigs', 'type': 'Book', 'description': 'child story'}
4 {'name': 'three pigs', 'type': 'Book', 'description': 'child story'}
5 {'name': 'two pigs', 'type': 'Book', 'description': 'child story'}
6 {'name': 'q', 'type': 'Book', 'description': 'nice'}
```
## 3.borrow by id
```
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
pls enter your option: 3
pls enter item id: 10000
id: 10000 processing...
item doesn't exist
```
## 4.return by id
```
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
pls enter your option: 4
pls enter item id: 11
id: 11 processing...
success
```
## 5.add new item
```
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
pls enter your option: 5
------------------------
   choose item type
------------------------
 1.Book
 2.Articles
 3.Digital Media
 q.quit to menu
pls enter your option: 1
pls enter name: booknow
pls enter desciption:now12345
pls enter authors, split by comma:me,you,he
```
## 6.upadate by id console putput
```
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
pls enter your option: 6
pls enter item id: 1
curr:: id: 1, name: three pigs
pls enter the option (name/description/save/q): name 
pls enter new value: nice
change staged:name:nice
pls enter the option (name/description/save/q): save
<saved>
```
## 7.delete by id console putput
```
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
pls enter your option: 7
pls enter item id: 1
curr:: id: 1, name: nice
delete? y/n: y
<saved>
```