import glob
import random
import string

from sqlalchemy import create_engine, MetaData
from sqlalchemyseed import HybridSeeder, load_entities_from_yaml
from sqlalchemy.orm import sessionmaker
from models.model import Base, User, Book, user_book_association

connection_string = 'postgresql+psycopg2://admin:admin@192.168.88.184/toaipostgres'
engine = create_engine(connection_string, echo=True)


Session = sessionmaker(bind=engine)
session = Session()
seeder = HybridSeeder(session, ref_prefix='!')

# Clear All table
meta = MetaData(bind=engine)
MetaData.reflect(meta)
for tbl in reversed(meta.sorted_tables):
    session.execute(f'DROP TABLE IF EXISTS "{tbl.name}"')
session.commit()

Base.metadata.create_all(bind=engine)

num_users = 100
num_books = 100


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# add users
for i in range(1, num_users + 1):
    username = f'user{i}'
    email = f'user{i}@example.com'
    password_hash = generate_random_string(10)
    user = User(username=username, email=email, password=password_hash)
    session.add(user)
    if i % 1000 == 0:
        session.commit()


for i in range(1, num_books + 1):
    title = f'Book {i}'
    book_id = i
    author = f'Author {random.randint(1, 100)}'
    price = round(random.uniform(10.0, 100.0), 2)
    book = Book(
        book_id=book_id,
        title=title,
        author=author,
        price=price
    )
    session.add(book)
    if i % 1000 == 0:
        session.commit()

session.commit()

users = session.query(User).all()
books = session.query(Book).all()

for index, user in enumerate(users):
    for _ in range(random.randint(1, 5)):
        book = random.choice(books)
        user.books.append(book)
        user_books_data = {
            'user_id': user.user_id,
            'book_id': book.book_id,
        }
        session.execute(user_book_association.insert().values(user_books_data))
    if index % 1000 == 0:
        session.commit()


# Seeding
yaml_files = glob.glob("seed/**/*.yaml", recursive=True)
for yaml_file in yaml_files:
    seeder.seed(load_entities_from_yaml(yaml_file))

seeder.session.commit()
