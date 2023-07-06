#!/usr/bin/python3
"""This module contains information about a user's work"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Work(BaseModel, Base):
    """Work model"""
    __tablename__ = 'works'

    title = Column(String(128), nullable=False)
    description = Column(String(255), nullable=True)
    image_url = Column(String(128), nullable=False)
    brand_id = Column(String(60), ForeignKey('brands.id'), nullable=False)
