from sqlalchemy import create_engine

#engine = create_engine('sqlite:///memory.db', echo = True)
engine = create_engine('mysql://root:clave@localhost/pruebasqlalchemy')
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(50))
    def __init__(self, name, fullname, password):
            self.name = name
            self.fullname = fullname
            self.password = password
    def __repr__(self):
            return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

Base.metadata.create_all(engine)

if __name__ == "__main__":
    
    from sqlalchemy.orm import sessionmaker

    #Session = sessionmaker(bind=engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    Session = sessionmaker()
    ##
    ed_user = User('reroes','rene rolando','2000')
    session.add(ed_user)
    session.commit()

