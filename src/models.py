from sqlalchemy import create_engine, Column, ForeignKey, Integer, Float, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import relationship
import settings
import pymysql

Base = declarative_base()

def db_connect():
    """
    Creates database connection using database settings from settings.py
    Returns sqlalchemy engine instance
    """
    print(URL(**settings.DATABASE))
    return create_engine(URL(**settings.DATABASE), echo=True)

def create_tables(engine):
    Base.metadata.create_all(engine)

class NbaGame(Base):
    __tablename__ = 'nba_game'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('nba_player.id'))
    date = Column(DateTime)
    opp = Column(String(15))
    away = Column(Boolean)
    score = Column(String(15))
    sec_played = Column(Integer)
    fgm = Column(Integer)
    fga = Column(Integer)
    fg_pct = Column(Float)
    three_pm = Column(Integer)
    three_pa = Column(Integer)
    three_pct = Column(Float)
    ftm = Column(Integer)
    fta = Column(Integer)
    ft_pct = Column(Float)
    off_reb = Column(Integer)
    def_reb = Column(Integer)
    total_reb = Column(Integer)
    ast = Column(Integer)
    to = Column(Integer)
    stl = Column(Integer)
    blk = Column(Integer)
    pf = Column(Integer)
    pts = Column(Integer)


class NbaPlayer(Base):
    __tablename__ = 'nba_player'

    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String(100))
    team = Column(String(20))
    pos = Column(String(20))
    height = Column(Integer)
    weight = Column(Integer)
    born = Column(DateTime)
    children = relationship("NbaGame")
