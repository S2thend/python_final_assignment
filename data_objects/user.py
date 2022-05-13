from util.constants import USER_FILE_URL
import csv
class User:
    def __init__(self, username:str, password:str) -> None:
        self.username = username
        self.password = password

    def __str__(self) -> str:
        return "username: " + self.username

    def read_users() -> list[dict]:
        '''
        return list[dict] 
        username:username
        password:password
        '''
        db = []
        try:
            with open(USER_FILE_URL, "r", newline="") as file:
                reader = csv.DictReader(file)
                db = reader
        except:
            # print("file users.csv doesn't exist") # DEBUG
            pass
        return db

    def save(self):
        try:
            db = User.read_users()
            headers = ["username","password"]
            # file doesn't exist or empty file go to except block
            if db == []:
                raise IOError
            # file is not empty then add new line to the end of the file
            with open(USER_FILE_URL, "a", newline="") as items_file:
                writer = csv.DictWriter(items_file, headers)
                writer.writerow({"username": self.username, "password": self.password })
        except IOError:
            # empty file write from start
            with open(USER_FILE_URL, "w", newline="") as items_file:
                writer = csv.DictWriter(items_file, headers)
                writer.writeheader()
                writer.writerow({"username": self.username, "password": self.password })