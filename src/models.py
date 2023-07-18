import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


# Usuario a Favorito es uno a muchos pues un usuario puede tener varios favoritos pero cada favorito es de solo un usuario
class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(250))
    lastname = Column(String(250))    
    username = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    favorite = relationship('Favorite', backref='user')


#Favoritos a planeta y personaje son relaciones de muchos a uno pues muchos registros de favoritos pueden referirse al mismo planeta o personaje pero cada
#registro de favoritos solo puede referirse a un planeta o personaje
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id =Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))


class Planet(Base):
    __tablename__= 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer, nullable = False)
    main_resource = Column(String(250), nullable=False)
    rotarion_period = Column(Integer, nullable = False)
    favorite = relationship('Favorite', backref='planet')



class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(Integer, nullable = False)
    height = Column(Integer, nullable = False)
    gender = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    favorite = relationship('Favorite', backref='character')



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
