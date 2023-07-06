#!/usr/bin/python3
"""Module that contains brand model"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship


class Brand(BaseModel, Base):
    """Brand model"""
    __tablename__ = 'brands'

    name = Column(String(49), nullable=False)
    handle = Column(String(15), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    address = Column(String(255), nullable=True)
    statement = Column(String(128), nullable=True)
    description = Column(String(255), nullable=True)
    is_solopreneur = Column(Boolean, default=False)
    cover_image = Column(String(128), nullable=True)
    detail_lead = Column(String(255), nullable=True)
    detail_image = Column(String(128), nullable=True)
    whatsapp_no = Column(String(15), nullable=True)
    twitter_url = Column(String(255), nullable=True)
    instagram_url = Column(String(255), nullable=True)
    youtube_url = Column(String(255), nullable=True)
    telegram_url = Column(String(255), nullable=True)

    detail_points = relationship("DetailPoint", cascade="all, delete",
                                 backref="brand")
    works = relationship("Work", cascade="all, delete", backref="brand")
