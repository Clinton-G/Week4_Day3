class Product():
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    
# Task 1 - And a method to display product information.
    def display_product_info(self):
        print(self.product_id)
        print(self.name)
        print(self.price)

# Task 2 - Create Subclasses: Book
class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)   # Task 3 - Calling the display method on an instance of any subclass shows both common and specific product details.
        self.product_id = product_id
        self.name = name            
        self.price = price
        self.author = author    # Task 2 - Subclass contains both inherited attributes from Product(id, name, price) and new attribute(author)


    def display_product_info(self):  # Task 3 - Calling the display method on an instance of any subclass shows both common and specific product details.
        print(self.product_id)
        print(self.name)
        print(self.price)
        print(self.author)



my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
my_book.display_product_info()