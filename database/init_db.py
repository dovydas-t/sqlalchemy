from database.db_connection import Base, engine
# Import all models to register them
from models.employee import Employee
from models.employer import Employer


# Create tables (this will ensure they exist)
Base.metadata.create_all(bind=engine)

print("Tables created successfully.")

def restart_db():
    """
    Function to refresh the database by dropping all tables and creating them again.
    """
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("Database refreshed successfully.")

def refresh_db():
    """
    Function to refresh the database by adding employer.id column on Employee inside database.
    """
    Base.metadata.create_all(bind=engine)