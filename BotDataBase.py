from BotConfigs import HOSTNAME, PORT, USERNAME, PASSWORD, DATABASE_NAME
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Integer, BigInteger, Enum, String, \
    Column
import enum
from sqlalchemy.orm import Session, sessionmaker

from BotLocalization import LOCALIZATIONS

Base = declarative_base()

engine : Engine = None

class job_types(enum.Enum):
    chief = 1
    servant = 2

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
    income = Column(BigInteger)
class human_deal(Base):
    __tablename__ = 'human_deals'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    last_name = Column(String(255))
    job_type = Column(Enum(job_types))
    cost = Column(Integer)
    income = Column(Integer)
    minimum_income = Column(Integer)


def Connect() -> Engine:
    global engine
    engine = create_engine("mysql+mysqldb://"+USERNAME+":"+PASSWORD+"@"+HOSTNAME+":"+str(PORT)+"/"+DATABASE_NAME, pool_size=10, pool_pre_ping=True)
    
    return engine

def update_user_settings(user_id: int, language: str):
    session = Session(bind=engine)
    settings = session.query(user_settings).filter(user_settings.user_id==user_id).first()
    if settings is None:
        return
    settings.language = language
    
    session.add(settings)
    session.commit()

def get_user_language(user_id: int) -> str:
    session = Session(bind=engine)
    settings = session.query(user_settings).filter(user_settings.user_id==user_id).first()
    if settings is None:
        return None
    return settings.language

def insert_new_user(user_id: int) -> bool:
    session = Session(bind=engine)
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
    session = Session(bind=engine)
    rest = session.query(restourant).filter(restourant.user_id==user_id).first()
    if rest is None:
        return
    rest.name = name
    session.add(rest)
    session.commit()

def get_income (user_id: int) -> int:
    session = Session(bind=engine)
    rest = session.query(restourant.income).filter(restourant.user_id==user_id).first()
    if rest is None:
        return 0
    return rest[0]

def get_available_human_deals (user_id: int, job_type: job_types):
    session = Session(bind=engine)
    deals = session.query(human_deal).filter(human_deal.job_type == job_type, human_deal.minimum_income <= get_income(user_id)).all()
    return deals
    