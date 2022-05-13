from util.constants import BORROW_LOG_FILE_URL
class BorrowService:
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