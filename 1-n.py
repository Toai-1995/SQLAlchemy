from sqlalchemy.orm import sessionmaker

from models.model import *
from Session import session

order = session.query(Order).filter(Order.order_id=='1').first()

order_item_1 = OrderItem(
    order_item_id=10,
    product_id=1,
    quantity=10,
    price=10.01,
)

order_item_2 = OrderItem(
    order_item_id=11,
    product_id=1,
    quantity=10,
    price=10.01,
)

order.order_items.extend([order_item_1, order_item_2])
# order1 = Order(
#     order_id=3,
#     user_id =1,
#     total_price=29.98,
#     status='Pending',
#     order_items=[
#         order_item_1, order_item_2
#     ]
# )

# session.add(order1)
order.status = 'Shipped'



print('toai', order_item_2.order.status)
# print('long', order.order_items)

session.commit()


