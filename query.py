from sqlalchemy.orm import lazyload, subqueryload, selectinload, raiseload, joinedload

from models.model import *
from Session import session

# # lazy loading
#
# users = session.query(User).all()
# for user in users:
#     print(user.username)
#     for book in user.books:
#         print(f"- {book.title}")
#
#
# # # eager loading
# users = session.query(User).options(joinedload(User.books)).all()
# for user in users:
#     print(user.username)
#     for book in user.books:
#         print(f"- {book.title}")
#
# # # subquery loading
# users = session.query(User).options(subqueryload(User.books)).all()
# for user in users:
#     print(user.username)
#     for book in user.books:
#         print(f"- {book.title}")

# # selectin loading
users = session.query(User).options(selectinload(User.books)).all()
for user in users:
    print(user.username)
    for book in user.books:
        print(f"- {book.title}")


