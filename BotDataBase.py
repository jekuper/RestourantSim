from BotConfigs import HOSTNAME, PORT, USERNAME, PASSWORD, DATABASE_NAME
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Integer, BigInteger, Enum, String, \
    Column
import enum
from sqlalchemy.orm import Session, sessionmaker
import json

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
class user_property(Base):
    __tablename__ = 'user_property'
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    balance = Column(Integer)
class restourant(Base):
    __tablename__ = 'restourants'
    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    name = Column(String(255))
    income = Column(BigInteger)
    workers = Column(String(16777215))
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
            income=0,
            workers="[]",
        )
        property = user_property(
            user_id=user_id,
            balance=500,
        )
        session.add_all([settings, rest, property])
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
def get_restourant(user_id: int):
    session = Session(bind=engine)
    rest = session.query(restourant).filter(restourant.user_id==user_id).first()
    return rest

def get_income (user_id: int) -> int:
    session = Session(bind=engine)
    rest = session.query(restourant.income).filter(restourant.user_id==user_id).first()
    if rest is None:
        return 0
    return rest[0]

def get_property (user_id: int) -> user_property:
    session = Session(bind=engine)
    rest = session.query(user_property).filter(user_property.user_id==user_id).first()
    if rest is None:
        return None
    return rest
def get_balance (user_id: int) -> int:
    session = Session(bind=engine)
    rest = session.query(user_property.balance).filter(user_property.user_id==user_id).first()
    if rest is None:
        return 0
    return rest[0]

def change_balance(user_id: int, delta: int):
    session = Session(bind=engine)
    property = session.query(user_property).filter(user_property.user_id==user_id).first()
    if property is None:
        return
    property.balance += delta
    session.add(property)
    session.commit()

def recalculate_income (user_id: int):
    session = Session(bind=engine)
    rest = session.query(restourant).filter(restourant.user_id==user_id).first()
    if rest is None:
        return
    workers = json.loads(rest.workers)
    incomes = session.query(human_deal.id, human_deal.income).filter(human_deal.id.in_(workers)).all()
    if incomes is None:
        return
    total_income = 0
    d = {}
    for e in incomes:
        d[e[0]] = e[1]
    for e in workers:
        total_income += d[e]

    rest.income = total_income
    session.add(rest)
    session.commit()
    
        

def get_workers(user_id: int) -> list[int]:
    session = Session(bind=engine)
    workers = session.query(restourant.workers).filter(restourant.user_id==user_id).first()
    if workers is None:
        return None
    return json.loads(workers[0])
def set_workers(user_id: int, new_list: list[int]):
    session = Session(bind=engine)
    rest = session.query(restourant).filter(restourant.user_id==user_id).first()
    if rest is None:
        return
    rest.workers = json.dumps(new_list)

    session.add(rest)
    session.commit()

def get_available_human_deals (user_id: int, job_type: job_types) -> list[human_deal]:
    session = Session(bind=engine)
    deals = session.query(human_deal).filter(human_deal.job_type == job_type, human_deal.minimum_income <= get_income(user_id)).all()
    return deals

def get_human_deal (id: int) -> human_deal:
    session = Session(bind=engine)
    deal = session.query(human_deal).filter(human_deal.id == id).first()
    return deal

def buy_human(user_id: int, deal: human_deal):
    if get_balance(user_id) < deal.cost:
        return
    change_balance(user_id, -deal.cost)

    workers = get_workers(user_id)
    workers.append(deal.id)
    set_workers(user_id, workers)
    recalculate_income(user_id)

