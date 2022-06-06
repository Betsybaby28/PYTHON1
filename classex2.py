class Book:
    def __init__(self,title,author,prize):
        self.title=title
        self.author=author
        self.prize=prize
    def view(self):
        print("title of book is %s,author name is %s and prize is %d" % (self.title, self.author, self.prize))
anu_book=Book("The girl","Dileep Kumar",300)
anu_book.view()
arun_book=Book("English poems","Anna Thomas",200)
arun_book.view()