class Book:
    def __init__(self,title,author,num_pages,current_page):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.current_page = current_page
        self.bookmarked_page = 1

    def move_bookmark(self):
        self.bookmarked_page = self.current_page

    def bookmark_diff_page(self,new_bookmark):
        self.bookmarked_page = new_bookmark        

    def turn_page(self, forward):
        if forward:
            if self.current_page == self.num_pages:
                self.current_page = 1
            else:
                self.current_page += 1
        else:
            self.current_page -= 1

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"
    
    def __len__(self):
        return self.num_pages

    def go_to_page(self,new_page):
        self.current_page = new_page   



book_1 = Book("Cats", "real person", 213, 1)  
#print(book_1.title)   


book_2 = Book("Dogs", "fake person", 198, 1)  
# print(book_2.title)      
# print(book_2.author)
# print(book_2.num_pages)


# book_1.go_to_page(42)
# print(book_1.current_page)

# print(book_1.bookmarked_page)

# book_1.bookmark_diff_page(50)
# print(book_1.bookmarked_page)


book_1.go_to_page(book_1.num_pages)
print()
print(book_1.current_page)

book_1.turn_page(True)

print(book_1.current_page)