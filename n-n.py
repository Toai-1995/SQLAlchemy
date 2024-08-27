from models.model import *
from Session import session

#
# # set up the relationship between user and book n-n
user = session.query(User).filter(User.user_id == 1).first()
book = session.query(Book).filter(Book.book_id == 1).first()
print("user", user.books)
print("book", book.users)
#
#
# # add relationship between user record and book record
#
# user1 = User(
#     username='toai',
#     user_id=100001,
#     email='toai1995@gmail.com',
#     password='123456'
# )
#
# book1 = Book(
#     book_id=100001,
#     title='Toai',
#     author='Toai',
#     price=100
# )
#
# session.add_all([user1, book1])
# user1.books.extend([book1])
#
# for user in book1.users:
#    print("Toai", user.username)
#
# session.commit()

# delete relationship between user record and book record
user5 = session.query(User).filter(User.user_id == 5).first()
session.delete(user5)
# print("user5", user5.books)
# user5.books.pop(0)


session.commit()








