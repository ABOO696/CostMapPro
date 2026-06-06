from app.database.base import Base
from app.database.session import engine

from app.database.models import *

Base.metadata.create_all(bind=engine)

print("All tables created.")