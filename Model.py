from sqlalchemy import Column, String, Integer, DECIMAL, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
import uuid
from database import Base


class User(Base):
    __tablename__ = "Users"

    user_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String(32), unique=True, nullable=False)
    display_name = Column(String(80), nullable=False)

    listings = relationship("Listing", back_populates="seller")


class Brand(Base):
    __tablename__ = "Brands"

    brand_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    country = Column(String(100))
    brand_image = Column(String(512))
    brand_url = Column(String(512))

    perfumes = relationship("Perfume", back_populates="brand")


class Perfume(Base):
    __tablename__ = "Perfumes"

    perfume_id = Column(Integer, primary_key=True, autoincrement=True)
    brand_id = Column(Integer, ForeignKey("Brands.brand_id"))
    name = Column(String(255), nullable=False)
    image = Column(String(512))

    brand = relationship("Brand", back_populates="perfumes")
    listings = relationship("Listing", back_populates="perfume")


class Listing(Base):
    __tablename__ = "Listings"

    listing_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    seller_id = Column(String, ForeignKey("Users.user_id"))
    perfume_id = Column(Integer, ForeignKey("Perfumes.perfume_id"))
    price = Column(DECIMAL(10, 2), nullable=False)
    condition = Column(String(50))
    status = Column(String(50), default="Active")
    description = Column(Text)
    type = Column(String(20))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    seller = relationship("User", back_populates="listings")
    perfume = relationship("Perfume", back_populates="listings")
    images = relationship("ListingImage", back_populates="listing")


class ListingImage(Base):
    __tablename__ = "ListingImages"

    listing_image_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    listing_id = Column(String, ForeignKey("Listings.listing_id"))
    image_url = Column(String(512), nullable=False)
    image_order = Column(Integer, nullable=False)

    listing = relationship("Listing", back_populates="images")
