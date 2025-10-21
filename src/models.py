import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
import enum
from datetime import datetime

db = SQLAlchemy()

class Character(db.Model):
    __tablename__ = 'character'
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(db.String(1000),nullable=True)
    image_url: Mapped[str] = mapped_column(db.String(250),nullable=True)
    name: Mapped[str] = mapped_column(db.String(50),nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }

class Planet(db.Model):
    __tablename__ = 'planet'
    id: Mapped[int] = mapped_column(primary_key=True)
    image_url: Mapped[str] = mapped_column(db.String(250),nullable=True)
    name: Mapped[str] = mapped_column(db.String(50),nullable=False)
    population: Mapped[int] = mapped_column(nullable=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
        }

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now, nullable=False)
    email: Mapped[str] = mapped_column(db.String(120), nullable=False)
    first_name: Mapped[str] = mapped_column(db.String(50), nullable=True)
    is_active: Mapped[bool] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(db.String(50), nullable=True)
    password: Mapped[str] = mapped_column(db.String(80), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now, nullable=False)
    user_name: Mapped[str] = mapped_column(db.String(50), nullable=False)
    
    favorites: Mapped[List["Favorite"]] = relationship(back_populates="user_item")
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.user_name,
            "email": self.email,
        }

class Favorite(db.Model):
    __tablename__ = 'favorite'
    id: Mapped[int] = mapped_column(primary_key=True)
    
    user_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"), nullable=False)
    planet_id: Mapped[int] = mapped_column(db.ForeignKey("planet.id"), nullable=True)
    character_id: Mapped[int] = mapped_column(db.ForeignKey("character.id"), nullable=True)
    
    user_item: Mapped["User"] = relationship(back_populates="favorites")
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "character_id": self.character_id,
        }

class AlembicVersion(db.Model):
    __tablename__ = 'alembic_version'
    version_num: Mapped[str] = mapped_column(db.String(32),primary_key=True)

