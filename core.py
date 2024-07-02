from sqlalchemy import create_engine, text

# connection_string = 'postgresql+psycopg2://admin:admin@192.168.1.87:5432/toaipostgres'
connection_string = 'postgresql+psycopg2://admin:admin@host.docker.internal/toaipostgres'
engine = create_engine(connection_string, echo=True)


with engine.connect() as connection:
    print("Connected to database")
    connection.execute(text('CREATE TABLE test (name char(30), age int)'))
    connection.execute(
        text("INSERT INTO test (name, age) VALUES ('Lolita', 18)")
    )
    # connection.commit()
