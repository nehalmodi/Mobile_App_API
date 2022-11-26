from database import engine,Base
from models import User,Contact

Base.metadata.create_all(bind=engine)