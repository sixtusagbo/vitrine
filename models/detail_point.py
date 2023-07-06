#!/usr/bin/python3
"""Points to support the detail lead"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class DetailPoint(BaseModel, Base):
    """Detail point model"""
    __tablename__ = 'detail_points'

    content = Column(String(128), nullable=False)
    brand_id = Column(String(60), ForeignKey('brands.id'), nullable=False)
