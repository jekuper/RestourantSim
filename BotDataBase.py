from BotConfigs import HOSTNAME, PORT, USERNAME, PASSWORD, DATABASE_NAME
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Integer, BigInteger, String, \
    Column
from sqlalchemy.orm import Session

from BotLocalization import LOCALIZATIONS

Base = declarative_base()

engine : Engine = None
session : Session = None

class user_settings(Base):
    __tablename__ = 'user_settings'
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    language = Column(String(255))
class restourant(Base):
    __tablename__ = 'restourants'
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    name = Column(String(255))


def Connect() -> Engine:
    global engine, session
    engine = create_engine("mysql+mysqldb://"+USERNAME+":"+PASSWORD+"@"+HOSTNAME+":"+str(PORT)+"/"+DATABASE_NAME)
    session = Session(bind=engine)
    return engine

def update_user_settings(user_id: int, language: str):
    global session
    settings = session.query(user_settings).filter(user_settings.user_id==user_id).first()
    if settings is None:
        return
    settings.language = language
    
    session.add(settings)
    session.commit()

def get_user_language(user_id: int) -> str:
    global session
    settings = session.query(user_settings).filter(user_settings.user_id==user_id).first()
    if settings is None:
        return None
    return settings.language

def insert_new_user(user_id: int) -> bool:
    global session
    settings = session.query(user_settings).filter(user_settings.user_id==user_id).first()
    if settings is None:
        settings = user_settings(
            user_id=user_id,
            language=LOCALIZATIONS[0],
        )
        rest = restourant(
            user_id=user_id,
            name="no_name",
        )
        session.add_all([settings, rest])
        session.commit()
        return True
    return False

def set_restourant_name(user_id: int, name: str):
    global session
    rest = session.query(restourant).filter(user_settings.user_id==user_id).first()
    if rest is None:
        return
    rest.name = name
    session.add(rest)
    session.commit()