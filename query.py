from sqlalchemy.orm import lazyload, subqueryload, selectinload, raiseload, joinedload

from models.model import Order, OrderItem, Book
from seed import session

order1 = session.query(Order).filter_by(order_id=1).first()

# books = session.query(Book).options(selectinload(Book.users)).all()

print('Long dep trai')

# print(books[0].users)
# print(order1.order_items)

order_item1 = session.query(OrderItem).filter_by(order_item_id=1).first()

# session.delete(order1)
# session.commit()

order1.order_items.remove(order_item1)
session.commit()
