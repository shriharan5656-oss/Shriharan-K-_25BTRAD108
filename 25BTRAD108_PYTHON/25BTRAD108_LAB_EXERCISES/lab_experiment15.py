class Book:
    def __init__(self, bid, title, author):
        self.bid, self.title, self.author, self.avail = bid, title, author, True
    def __str__(self):
        return f"[{self.bid}] {self.title} by {self.author} ({'Available' if self.avail else 'Issued'})"

class ReferenceBook(Book):
    def __init__(self, bid, title, author, edition):
        super().__init__(bid, title, author)
        self.edition = edition

class Library:
    def __init__(self, name):
        self.name, self.books = name, {}

    def add_book(self, b):
        self.books[b.bid] = b
        print(f"Added: {b.title}")

    def issue_book(self, bid):
        b = self.books.get(bid)
        if not b: return print(f"Error: {bid} not found.")
        if isinstance(b, ReferenceBook) or not b.avail:
            return print(f"Issue denied for '{b.title}'.")
        b.avail = False
        print(f"Issued: '{b.title}'")

    def return_book(self, bid):
        b = self.books.get(bid)
        if b and not b.avail:
            b.avail = True
            print(f"Returned: '{b.title}'")

    def display(self):
        print(f"\n--- Catalog: {self.name} ---")
        for b in self.books.values(): print(b)

if __name__ == "__main__":
    lib = Library("Central Library")
    lib.add_book(Book("B101", "Clean Code", "Robert C. Martin"))
    lib.add_book(ReferenceBook("R901", "Dictionary", "Oxford", "11th"))
    
    lib.display()
    lib.issue_book("B101")
    lib.issue_book("R901")  # Denied (reference)
    lib.return_book("B101")
    lib.display()
