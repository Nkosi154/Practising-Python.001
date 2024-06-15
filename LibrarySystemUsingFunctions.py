'''Library Management System:

Description: This system helps manage the operations of a library, including adding new books, borrowing books, returning books.
Operations:
.Add a new book to the library inventory.
.Allow users to borrow books, ensuring they are available.
.Accept returned books and update the inventory.'''


print("****************************")
print("Library Management System")
print("****************************")

Books = ["Mommy Tale" , "Forest Monster","Boogy Man","The Lost Sherperd"]

print("****************************")
print("Choose from this options.")
print("1.Checking for book name.")
print("2.Returning a book.")
print("3.Add books in the inventory.")
print("****************************")

def options():
 while True:
  Choice = int(input("Choose a number from 1-3: "))
  if  1 <= Choice <= 3:
     
    return Choice
    
  else:
    print("Invalid Choice! , Choose a number from 1-3.")
   

def check_books():
  while True:
     
     print("List of Books available: ", Books)
     new_book = input("Enter Book title of the book you looking for: ")
     if isinstance(new_book,str):
        if new_book in Books:
          print("Book is available!")
          Books.remove(new_book)
          break
        else:
          print("Book is not available!")
          print("Choose from this List: ",Books)

          
def returning_books():
   
     returned_book =input("Enter the Title of Book to return or Write (Exit) if you want to exit : ")
     if returned_book == "Exit":
          print("Thank you for using the system bye!")
          
     else:
       Books.append(returned_book)
       print("Books available " ,Books)
     
def add_newbook():
   
    newbook = input("What is the name of the new book you want to add: ")
    if isinstance(newbook,str):
      Books.append(newbook)
      print("The List of books available: ", Books)

Choice = options()

if Choice == 1:
    check_books()
elif Choice == 2:
    returning_books()
elif Choice == 3:
    add_newbook()

