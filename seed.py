import glob
from sqlalchemy import create_engine, MetaData
from sqlalchemyseed import HybridSeeder, load_entities_from_yaml
from sqlalchemy.orm import sessionmaker
from models.model import Base

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


# Seeding
yaml_files = glob.glob("seed/**/*.yaml", recursive=True)
for yaml_file in yaml_files:
    seeder.seed(load_entities_from_yaml(yaml_file))

seeder.session.commit()
