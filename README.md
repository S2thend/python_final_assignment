# python_final_assignment
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


# User Manual
## 2.list by type console putput
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