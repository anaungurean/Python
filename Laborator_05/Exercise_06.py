'''
Ex06. Design a library catalog system with a base class LibraryItem and subclasses for different types of items like Book, DVD, and Magazine.
Include methods to check out, return, and display information about each item.
'''

class LibraryItem:
    existing_id = set()
    def __init__(self, id, title, author, year, genre, status):
        if id in LibraryItem.existing_id:
            raise ValueError(f"The id {id} is already used.")
        self.id = id
        LibraryItem.existing_id.add(id)
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.status = status

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def check_out(self):
        self.status = "checked_out"

    def return_item(self):
        self.status = "available"

    def is_for_children(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def display_info(self):
        print(f"Id: {self.id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Genre: {self.genre}")
        print(f"Status: {self.status}")

class Book(LibraryItem):
    def __init__(self, id, title, author, year, genre, status, pages, colour_of_cover , illustrations):
        super().__init__(id, title, author, year, genre, status)
        self.pages = pages
        self.colour_of_cover = colour_of_cover
        self.illustrations = illustrations

    def set_pages(self, pages):
        self.pages = pages

    def get_pages(self):
        return self.pages

    def set_colour_of_cover(self, colour_of_cover):
        self.colour_of_cover = colour_of_cover

    def get_colour_of_cover(self):
        return self.colour_of_cover

    def bookmark_page(self, page_number):
        return f"Bookmark added to page {page_number} in {self.title}."

    def find_chapter(self, chapter_name):
        return f"Finding chapter '{chapter_name}' in {self.title}."

    def check_for_illustrations(self):
        if self.illustrations:
            return f"{self.title} has illustrations."
        else:
            return f"{self.title} does not have illustrations."

    def is_for_children(self):
        if self.illustrations and self.pages < 100 and self.colour_of_cover == "colourful" and self.genre == "children":
            return f"{self.title} is for children."
        else:
            return f"{self.title} is not for children."

    def display_info(self):
        super().display_info()
        print(f"Pages: {self.pages}")

class DVD(LibraryItem):
    def __init__(self, id, title, author, year, genre, status, length):
        super().__init__(id, title, author, year, genre, status)
        self.length = length

    def set_length(self, length):
        self.length = length

    def get_length(self):
        return self.length

    def display_info(self):
        super().display_info()
        print(f"Length: {self.length}")

    def play_dvd(self):
        return f"Playing the DVD {self.title}."

    def display_duration(self):
        return f"The duration of {self.title} is {self.length} minutes."

    def is_for_children(self):
        if self.length < 60 and self.genre == "children":
            return f"{self.title} is for children."
        else:
            return f"{self.title} is not for children."

class Magazine(LibraryItem):
    def __init__(self, id, title, author, year, genre, status, issue, pages, colour_of_cover, illustrations):
        super().__init__(id, title, author, year, genre, status)
        self.issue = issue
        self.pages = pages
        self.colour_of_cover = colour_of_cover
        self.illustrations = illustrations

    def set_issue(self, issue):
        self.issue = issue

    def get_issue(self):
        return self.issue

    def set_pages(self, pages):
        self.pages = pages

    def get_pages(self):
        return self.pages

    def set_colour_of_cover(self, colour_of_cover):
        self.colour_of_cover = colour_of_cover

    def get_colour_of_cover(self):
        return self.colour_of_cover

    def set_illustrations(self, illustrations):
        self.illustrations = illustrations

    def get_illustrations(self):
        return self.illustrations

    def is_for_children(self):
        if self.illustrations and self.pages < 100 and self.colour_of_cover == "colourful" and self.genre == "children":
            return f"{self.title} is for children."
        else:
            return f"{self.title} is not for children."

    def display_info(self):
        super().display_info()
        print(f"Issue: {self.issue}")

    def browse_articles(self):
        return f"Browsing articles in {self.title}, Issue {self.issue}."

    def read_article(self, article_name):
        return f"Reading the article '{article_name}' in {self.title}, Issue {self.issue}."