class Page(object):
    def __init__(self,page_number,content):
        self.page_number = page_number
        self.content = content

    def read(self):#instance method
        print(f"Reading {self.content} of page number {self.page_number}")

    @staticmethod
    def print_to_printer(content):#static method
        print(f"printing......")
        print(content)
    # def __str__(self):
    #     return self.content
    def __repr__(self):#represents how the object will print in console
        return self.content
# p = Page(1, "This is new paragraph.")
# p.read()
# Page.print_to_printer("This is sentence.")

class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages

    def number_of_pages(self):
        return len(self.pages)

    def add_pages(self,page):
        self.pages.append(page)
    
    def get_content(self,page_number):
        for i in self.pages:
            if page_number == i.page_number:
                return i.content
        return "page not found"

    def __str__(self):
        return self.title

pages = []
for i in range(1,6):
    p = Page(i,f"This is paragraph {i}.")
    pages.append(p)

b = Book("Math",pages)
# print(f"Number of pages: {b.number_of_pages()}")

p = Page(6,"This is new page")
b.add_pages(p)
# print(f"Number of pages: {b.number_of_pages()}")
# print(b)
# print(p)
# print(b.pages)
# print(b.get_content(6))

#print(b.__dict__) represents the object in dictionary