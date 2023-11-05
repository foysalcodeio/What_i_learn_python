class StoryBook:
    #class variable
    no_of_books = 0
    
    discount = 0.5
    # a special method is used for sitting the instance
    # self atumatic pass value. its look like 
    def __init__(self, name, age, price, year):
        self.name = name
        self.age = age
        self.price = price
        self.year = year
        StoryBook.no_of_books += 1
    
    #regular method - 1
    def get_book_info(self):
        print(f'The Book name : {self.name} The Book age : {self.age} The Book price : {self.price}')

    #regular method - 2
    def get_book_price(self):
        print(f'The Book price : {self.price}')

    #applying discount to an instance
    def apply_discount(self):
        self.price = int(self.price - self.price * self.discount)

    #method to change price
    def set_price(self, new_price):
        self.price = new_price
        
    #class method 1
    @classmethod
    def set_discount(cls, new_discount):
        cls.discount = new_discount

# creating an instance/object of the class
book_1 = StoryBook("Harry Potter", 20, 100, 2012)
book_2 = StoryBook("Titanic", 30, 200, 1996)
print(book_1.name + " " + str(book_1.age) + " " + str(book_1.price) + " " + str(book_1.year))


# class.method(obj)
StoryBook.get_book_price(book_2)

#obj.method
book_1.get_book_info()


print(book_1.no_of_books)
print(book_2.no_of_books)
print(StoryBook.no_of_books)

print('Book price : ', book_2.price)
book_2.apply_discount()
print('After discount Book price : ', book_2.price)

print('class method book price -> ', book_1.price)
print('class method book discount -> ', book_1.discount)
StoryBook.set_discount(0.25)
book_1.apply_discount()
print(book_1.price)

