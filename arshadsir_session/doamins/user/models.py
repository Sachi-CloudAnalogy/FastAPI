from sqlalchemy import Column, String, Integer

class User(Base):
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    password = Column(String, nullable=False)