from backend.db.session import engine
from backend.db.base_class import Base
from backend.models import associations, db_groups, db_series

def create_all_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")

if __name__ == "__main__":
    create_all_tables()