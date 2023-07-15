#!/usr/bin/python3
"""Module that contains brand model"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from passlib.apps import custom_app_context as pwd_context
from models.helpers import MySerializer
from itsdangerous.exc import BadSignature, SignatureExpired
import models


class Brand(BaseModel, Base):
    """Brand model"""

    __tablename__ = "brands"

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
    token = Column(String(128), nullable=True)

    detail_points = relationship(
        "DetailPoint", cascade="all, delete", backref="brand"
    )
    works = relationship("Work", cascade="all, delete", backref="brand")

    def to_dict(self, with_works=False):
        """Return modified version of the inherited to_dict"""
        result = super(Brand, self).to_dict()

        result["detail_points"] = []
        for detail_point in self.detail_points:
            result["detail_points"].append(detail_point.content)
        if with_works:
            result["works"] = [work.to_dict() for work in self.works]

        return result

    def hash_password(self, password):
        """Hash password"""
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        """Verify password"""
        return pwd_context.verify(password, self.password)

    def generate_auth_token(self, secret_key):
        """Generate authentication token"""
        s = MySerializer(secret_key)
        return s.dumps({"handle": self.handle})

    @staticmethod
    def verify_auth_token(token, secret_key, expiration=600):
        """Return user if token is valid"""
        s = MySerializer(secret_key)
        try:
            data = s.loads(token, max_age=expiration)
        except SignatureExpired:
            handle = s.loads(token).get("handle")
            user = models.storage.get_brand(handle)
            user.token = None
            user.save()
            return user
        except BadSignature:
            # invalid token
            return None
        user = models.storage.get_brand(data["handle"])
        return user

    @property
    def is_active(self):
        """True, as all users are active"""
        return True

    def get_id(self):
        """Return the token that can be used to reload the user"""
        return self.token

    @property
    def is_authenticated(self):
        """Return true if user is authenticated"""
        return True if self.token else False

    @property
    def is_anonymous(self):
        """Anonymous users are not supported"""
        return False

    @property
    def is_new(self):
        """Check if a user is new"""
        return (
            True
            if not self.statement
            and not self.description
            and not self.cover_image
            else False
        )
