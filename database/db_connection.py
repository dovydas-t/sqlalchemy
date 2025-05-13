from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

username = "root"
password = "MySqlRootPassword.123"
host = "localhost"
port = 3306
database = "test_db1"


engine = create_engine(f"mysql://{username}:{password}@{host}:{port}/{database}")
SessionLocal = sessionmaker(bind=engine)
