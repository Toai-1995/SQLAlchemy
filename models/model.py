from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Column, String, Integer, Table, TIMESTAMP, TEXT, DECIMAL, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()

user_book_association = Table('user_book_association', Base.metadata,
                              Column('user_id', Integer, ForeignKey('users.user_id')),
                              Column('book_id', Integer, ForeignKey('books.book_id'))
                              )

user_toy_association = Table('user_toy_association', Base.metadata,
                             Column('user_id', Integer, ForeignKey('users.user_id')),
                             Column('toy_id', Integer, ForeignKey('toys.toy_id'))
                             )


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    orders = relationship('Order', back_populates='user', uselist=True)
    reviews = relationship('Review', back_populates='user', uselist=True)
    books = relationship('Book', secondary=user_book_association, back_populates='users', uselist=True)
    toys = relationship('Toy', secondary=user_toy_association, back_populates='users', uselist=True)


class Category(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    books = relationship('Book', back_populates='category', uselist=True, )
    toys = relationship('Toy', back_populates='category', uselist=True)


class Book(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Column(TEXT)
    price = Column(DECIMAL, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    created_at = Column(DateTime, default=datetime.now)

    category = relationship('Category', back_populates='books', cascade='all, delete')
    reviews = relationship('Review', back_populates='book', uselist=True)
    users = relationship('User', secondary=user_book_association, back_populates='books', uselist=True)


class Toy(Base):
    __tablename__ = 'toys'
    toy_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    description = Column(TEXT)
    price = Column(DECIMAL, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    created_at = Column(DateTime, default=datetime.now)

    category = relationship('Category', back_populates='toys')
    reviews = relationship('Review', back_populates='toy', uselist=True)
    users = relationship('User', secondary=user_toy_association, back_populates='toys', uselist=True)


class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    total_price = Column(DECIMAL, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    user = relationship('User', back_populates='orders')
    order_items = relationship('OrderItem', back_populates='order', uselist=True)


class OrderItem(Base):
    __tablename__ = 'order_items'
    order_item_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'))
    product_id = Column(Integer, nullable=False)  # Can be book_id or toy_id
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL, nullable=False)

    order = relationship('Order', back_populates='order_items')


class Review(Base):
    __tablename__ = 'reviews'
    review_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    book_id = Column(Integer, ForeignKey('books.book_id'), nullable=True)
    toy_id = Column(Integer, ForeignKey('toys.toy_id'), nullable=True)
    rating = Column(Integer, nullable=False)
    comment = Column(TEXT)
    created_at = Column(DateTime, default=datetime.now)

    user = relationship('User', back_populates='reviews')
    book = relationship('Book', back_populates='reviews', uselist=False)
    toy = relationship('Toy', back_populates='reviews', uselist=False)


class Cart(Base):
    __tablename__ = 'cart'
    cart_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    product_id = Column(Integer, nullable=False)  # Can be book_id or toy_id
    quantity = Column(Integer, nullable=False)

    user = relationship('User')
