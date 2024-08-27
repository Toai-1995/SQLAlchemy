import time

from sqlalchemy.orm import lazyload, subqueryload, selectinload, raiseload, joinedload, noload, contains_eager

from models.model import *
from Session import session

# lazy loading

# users = session.query(User).all()
# for user in users:
#     print(user.username)
#     for book in user.books:
#         print(f"- {book.title}")


# # eager loading
# users = session.query(User).options(joinedload(User.books)).all()
# for user in users:
#     print(user.username)
#     for book in user.books:
#         print(f"- {book.title}")

# # subquery loading
# users = session.query(User).options(subqueryload(User.books)).all()
# for user in users:
#     print(user.username)
#     for book in user.books:
#         print(f"- {book.title}")

# # selectin loading
# users = session.query(User).options(selectinload(User.books)).all()
# for user in users:
#     print(user.username)
#     for book in user.books:
#         print(f"- {book.title}")

# # raise loading
# users = session.query(User).options(raiseload(User.books)).all()
# for user in users:
#     print(user.username)
#     for book in user.books:
#         print(f"- {book.title}")

# # no loading
# users = session.query(User).options(noload(User.books)).all()
# for user in users:
#     print(user.username)
#     print(user.books)

# contains_eager
# users = session.query(User).join(User.books).options(contains_eager(User.books)).all()
# for user in users:
#     print(user.username)
#     for book in user.books:
#         print(f"- {book.title}")

# start_time = time.time()
# users = session.query(User).options(joinedload(User.books)).all()
# elapsed_time = time.time() - start_time
# print(f"Thời gian thực thi với joinedload: {elapsed_time:.5f} giây")

# start_time = time.time()
# users = session.query(User).options(subqueryload(User.books)).all()
# elapsed_time = time.time() - start_time
# print(f"Thời gian thực thi với subqueryload: {elapsed_time:.5f} giây")

# start_time = time.time()
# users = session.query(User).options(selectinload(User.books)).all()
# elapsed_time = time.time() - start_time
# print(f"Thời gian thực thi với subqueryload: {elapsed_time:.5f} giây")

# start_time = time.time()
# users = session.query(User).options(lazyload(User.books)).all()
# for user in users:
#     for book in user.books:
#         pass
# elapsed_time = time.time() - start_time
# print(f"Thời gian thực thi với subqueryload: {elapsed_time:.5f} giây")

