from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


connection_string = 'postgresql+psycopg2://admin:admin@192.168.88.184/toaipostgres'
engine = create_engine(connection_string, echo=True)


Session = sessionmaker(bind=engine)
session = Session()
