#Base class Library item
class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def display_info(self):
        return f"Title:{self.title}, Author:{self.author}"

#subclass book
class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title, author) #inheritance from base class
    
    def display_info(self):
        return f"|Book:|  {super().display_info()}"

#subclass magazine    
class Magazine(LibraryItem):
    def __init__(self, title, author, issue_frequence):
        super().__init__(title, author) #inheritance from base class
        self.issue_frequence = issue_frequence #add extra attribute 

    def display_info(self):
        return f"|Magazine:|  {super().display_info()}, Issue Frequence:{self.issue_frequence}" 
    

# new class library to add remove and display items
class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item): #add item using append
        self.items.append(item)

    def remove_item(self, title): #remove item with for loop
        self.items = [item for item in self.items if item.title != title]

    def display_all(self): #display all items
        for item in self.items:
            print(item.display_info())

