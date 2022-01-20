class Library:

    def __init__(self,listOfBooks):
        self.books=listOfBooks     

    def displayAvailableBooks(self):
        print("Bookes present in this library are: ")
        for book in self.books:
            print("\t * " + book)

    def borrowBooks(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}, please keep it safe and returned it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print(f"Sorry, Book {bookName} is either not available or already issued to some else, please wait until the book is available")
            return False
    
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book, Hope You enjoyed reading this")

class Student:
    def requestBook(self):
        self.Book=input("Please Enter name of book you want to borrw: ")
        return self.Book

    def returnBook(self):
        self.Book=input("Please Enter name of book you want to return: ")
        return self.Book

if __name__=="__main__":
    centralLibrary=Library(['Algorthim','Django','Clrs','Python'])
    Student=Student()
    

    # making menu using infinite loop
    while (True):
        welcomeMessage='''
        ===Welcome to Central Library===
        Please Choose an option
        1: List all the books
        2: Request a book
        3: Add/Return a book
        4: Exit the library
        '''
        print(welcomeMessage)

        a=int(input("Enter a choice: "))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBooks(Student.requestBook())
        elif a==3:
            centralLibrary.returnBook(Student.returnBook())
        elif a==4:
            print("Thanks for choosing central library, Have agreat day ahead")
            exit()
        else:
            print("Invalid Choice")

        
       


