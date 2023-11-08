from BotConfigs import HOSTNAME, PORT, USERNAME, PASSWORD, DATABASE_NAME, SOCKET_LOCATION
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Integer, BigInteger, Enum, String, DateTime, \
    Column
from sqlalchemy.dialects.mysql import MEDIUMINT
import enum
from sqlalchemy.orm import Session
import json
from sqlalchemy.sql import func
import datetime
import random

from BotLocalization import LOCALIZATIONS, PHRASES

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
    last_active = Column(DateTime(timezone=True), server_default=func.now())
    income = Column(BigInteger)
    workers = Column(String(16777215))
    kitchen_workload = Column(MEDIUMINT)
    kitchen_workload_max = Column(MEDIUMINT)
    lounge_workload = Column(MEDIUMINT)
    lounge_workload_max = Column(MEDIUMINT)
    tax_debt = Column(Integer)
    brawl_damage = Column(Integer)

class human_deal(Base):
    __tablename__ = 'human_deals'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    last_name = Column(String(255))
    job_type = Column(Enum(job_types))
    cost = Column(Integer)
    income = Column(Integer)
    minimum_income = Column(Integer)

def bool_based_on_probability(probability=0.5) -> bool:
    return random.random() < probability

def random_float(minInclusive, maxInclusive) -> float:
    return random.uniform(minInclusive, maxInclusive)

def Connect() -> Engine:
    global engine

    if SOCKET_LOCATION is None:
        engine = create_engine(f"mysql+mysqldb://{USERNAME}:{PASSWORD}@{HOSTNAME}:{str(PORT)}/{DATABASE_NAME}", pool_size=10, pool_pre_ping=True)
    else:
        engine = create_engine(f"mysql+mysqldb://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DATABASE_NAME}?unix_socket={SOCKET_LOCATION}", pool_size=10, pool_pre_ping=True)
    
    return engine
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
            last_active=datetime.datetime(2000, 1, 1, 0, 0, 0, 0),
            workers="[]",
            kitchen_workload = 0,
            kitchen_workload_max = 5,
            lounge_workload = 0,
            lounge_workload_max = 5,
            tax_debt = 0,
            brawl_damage = 0,
        )
        property = user_property(
            user_id=user_id,
            balance=500,
        )
        session.add_all([settings, rest, property])
        session.commit()
        return True
    return False


#region user_settings
def update_user_language(user_id: int, language: str):
    session = Session(bind=engine)
    settings = session.query(user_settings).filter(user_settings.user_id==user_id).first()
    if settings is None:
        return
    settings.language = language
    
    session.add(settings)
    session.commit()
def get_user_language(user_id: int) -> str:
    session = Session(bind=engine)
    settings = session.query(user_settings.language).filter(user_settings.user_id==user_id).first()
    if settings is None:
        return None
    return settings[0]
def get_user_settings(user_id: int) -> user_settings:
    session = Session(bind=engine)
    settings = session.query(user_settings).filter(user_settings.user_id==user_id).first()
    if settings is None:
        return None
    return settings
#endregion

#region restourant
def set_restourant_name(user_id: int, name: str):
    session = Session(bind=engine)
    rest = session.query(restourant).filter(restourant.user_id==user_id).first()
    if rest is None:
        return
    rest.name = name
    session.add(rest)
    session.commit()
def get_restourant(user_id: int) -> restourant:
    session = Session(bind=engine)
    rest = session.query(restourant).filter(restourant.user_id==user_id).first()
    return rest

def get_income (user_id: int) -> int:
    session = Session(bind=engine)
    rest = session.query(restourant.income).filter(restourant.user_id==user_id).first()
    if rest is None:
        return 0
    return rest[0]
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
def recalculate_workload (user_id: int):
    session = Session(bind=engine)
    rest = session.query(restourant).filter(restourant.user_id==user_id).first()
    if rest is None:
        return
    workers = json.loads(rest.workers)
    jobs = session.query(human_deal.id, human_deal.job_type).filter(human_deal.id.in_(workers)).all()
    if jobs is None:
        return
    d = {}
    k_workload = 0
    l_workload = 0
    for e in jobs:
        d[e[0]] = e[1]
    for e in workers:
        if d[e] == job_types.chief:
            k_workload += 1
        else:
            l_workload += 1

    rest.kitchen_workload = k_workload
    rest.lounge_workload = l_workload
    session.add(rest)
    session.commit()
    
def get_workers(user_id: int) -> list[int]:
    session = Session(bind=engine)
    workers = session.query(restourant.workers).filter(restourant.user_id==user_id).first()
    if workers is None:
        return None
    return json.loads(workers[0])
def workers_to_string(employees: list[int]) -> list[str]:
    session = Session(bind=engine)
    result = session.query(func.concat(human_deal.name, " ", human_deal.last_name)).filter(human_deal.id.in_(employees)).all()
    if result is None:
        return None
    return json.loads(result)
def set_workers(user_id: int, new_list: list[int]):
    session = Session(bind=engine)
    rest = session.query(restourant).filter(restourant.user_id==user_id).first()
    if rest is None:
        return
    rest.workers = json.dumps(new_list)

    session.add(rest)
    session.commit()
def get_kitchen_stats(user_id: int):
    session = Session(bind=engine)
    rest = session.query(restourant.kitchen_workload, restourant.kitchen_workload_max).filter(restourant.user_id==user_id).first()
    if rest is None:
        return [0, -1]
    return rest
def get_lounge_stats(user_id: int):
    session = Session(bind=engine)
    rest = session.query(restourant.lounge_workload, restourant.lounge_workload_max).filter(restourant.user_id==user_id).first()
    if rest is None:
        return [0, -1]
    return rest
def extend_kitchen(user_id: int):
    session = Session(bind=engine)
    rest = session.query(restourant).filter(restourant.user_id==user_id).first()
    if rest is None:
        return
    rest.kitchen_workload_max += 5

    session.add(rest)
    session.commit()

def extend_lounge(user_id: int):
    session = Session(bind=engine)
    rest = session.query(restourant).filter(restourant.user_id==user_id).first()
    if rest is None:
        return
    rest.lounge_workload_max += 5

    session.add(rest)
    session.commit()
def can_buy_k(user_id: int):
    rest = get_restourant(user_id)
    return rest.kitchen_workload < rest.kitchen_workload_max
def can_buy_l(user_id: int):
    rest = get_restourant(user_id)
    return rest.lounge_workload < rest.lounge_workload_max

def record_active(user_id: int):
    session = Session(bind=engine)
    rest = session.query(restourant).filter(restourant.user_id==user_id).first()
    if rest is None:
        return
    rest.last_active = func.now()

    session.add(rest)
    session.commit()
def get_last_active (user_id: int) -> datetime.datetime:
    session = Session(bind=engine)
    rest = session.query(restourant.last_active).filter(restourant.user_id==user_id).first()
    if rest is None:
        return 0
    return rest[0]
def can_start_shift(user_id: int) -> bool:
    last = get_last_active(user_id)
    dif = datetime.datetime.now() - last
    if dif.total_seconds() >= 3600 * 3:
        return True
    return False
def get_wait_time(user_id: int) -> datetime.timedelta:
    last = get_last_active(user_id)
    dif = datetime.datetime.now() - last
    return datetime.timedelta(seconds=3600 * 3 - dif.total_seconds())

def change_debt(user_id: int, delta: int):
    session = Session(bind=engine)
    rest = session.query(restourant).filter(restourant.user_id==user_id).first()
    if rest is None:
        return
    rest.tax_debt += delta
    session.add(rest)
    session.commit()
def nullify_debt(user_id: int):
    session = Session(bind=engine)
    rest = session.query(restourant).filter(restourant.user_id==user_id).first()
    if rest is None:
        return
    rest.tax_debt = 0
    session.add(rest)
    session.commit()
def get_debt (user_id: int) -> int:
    session = Session(bind=engine)
    rest = session.query(restourant.tax_debt).filter(restourant.user_id==user_id).first()
    if rest is None:
        return 0
    return rest[0]
def get_total_debt(user_id: int) -> int:
    if get_debt(user_id) == 0:
        return 0
    return get_debt(user_id) * 2 + (get_balance(user_id) // 2)

def change_brawl_damage(user_id: int, delta: int):
    session = Session(bind=engine)
    rest = session.query(restourant).filter(restourant.user_id==user_id).first()
    if rest is None:
        return
    rest.brawl_damage += delta
    session.add(rest)
    session.commit()
def nullify_brawl_damage(user_id: int):
    session = Session(bind=engine)
    rest = session.query(restourant).filter(restourant.user_id==user_id).first()
    if rest is None:
        return
    rest.brawl_damage = 0
    session.add(rest)
    session.commit()
def get_brawl_damage (user_id: int) -> int:
    session = Session(bind=engine)
    rest = session.query(restourant.brawl_damage).filter(restourant.user_id==user_id).first()
    if rest is None:
        return 0
    return rest[0]
#endregion

#region property
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
    session.close()
#endregion  

#region human deals
def get_available_human_deals (user_id: int, job_type: job_types) -> list[human_deal]:
    session = Session(bind=engine)
#    deals = session.query(human_deal).filter(human_deal.job_type == job_type, human_deal.minimum_income <= get_income(user_id)).all()
    deals = session.query(human_deal).filter(human_deal.job_type == job_type).all()
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
    recalculate_workload(user_id)
#endregion
