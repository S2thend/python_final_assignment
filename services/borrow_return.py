from pkgutil import walk_packages
from util.constants import BORROW_LOG_FILE_URL, BORROW_TYPE, RETURN_TYPE
from datetime import datetime
import csv
class BorrowReturnService:
    def __read_log_all(self):
        db = []
        try:
            with open(BORROW_LOG_FILE_URL, "r", newline="") as file:
                reader = csv.DictReader(file)
                for item in reader:
                    db.append(item)
        except:
            # print("file borrow_log.csv doesn't exist") # DEBUG
            pass
        return db

    def __find_unreturned_items(self) -> set:
        db = self.__read_log_all()
        unreturned = set()
        for item in db:
            if item["action"] == BORROW_TYPE:
                unreturned.add(item["item_id"])
            elif item["action"] == RETURN_TYPE:
                unreturned.remove(item["item_id"])
        return unreturned


    def __log(self,username,id,action):
        '''
        action log
        '''
        headers = ["username", "item_id", "action", "date"]
        try:
            db = self.__read_log_all()
            # if file no existance or empty go to except block
            if len(db) == 0:
                raise IOError
            # save using the same id used for items file
            with open(BORROW_LOG_FILE_URL, "a", newline="") as file:
                writer = csv.DictWriter(file, headers)
                writer.writerow({"username": username, "item_id": id, "action":action, "date":datetime.now().strftime("%m/%d/%Y, %H:%M:%S") })
        except IOError:
            with open(BORROW_LOG_FILE_URL, "w", newline="") as file:
                writer = csv.DictWriter(file, headers)
                writer.writeheader()
                writer.writerow({"username": username, "item_id": id, "action":action, "date":datetime.now().strftime("%m/%d/%Y, %H:%M:%S") })

    def log_borrow(self,username,id,db):
        unreturned = self.__find_unreturned_items()
        if id in unreturned:
            print("cant borrow unreturned items")
        elif id in db:
            self.__log(username,id,BORROW_TYPE)
            print("success")
        else:
            print("item doesn't exist")

    def log_return(self,username,id):
        unreturned = self.__find_unreturned_items()
        if id in unreturned:
            self.__log(username,id,RETURN_TYPE)
            print("success")
        else:
            print("cant return unborrowed items")