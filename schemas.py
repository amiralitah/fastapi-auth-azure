from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

# ---- USERS ----
class UserBase(BaseModel):
    username: str
    display_name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    user_id: str
    class Config:
        orm_mode = True


# ---- BRANDS ----
class BrandBase(BaseModel):
    name: str
    country: Optional[str] = None
    brand_image: Optional[str] = None
    brand_url: Optional[str] = None

class BrandCreate(BrandBase):
    pass

class Brand(BrandBase):
    brand_id: int
    class Config:
        orm_mode = True


# ---- PERFUMES ----
class PerfumeBase(BaseModel):
    brand_id: int
    name: str
    image: Optional[str] = None

class PerfumeCreate(PerfumeBase):
    pass

class Perfume(PerfumeBase):
    perfume_id: int
    class Config:
        orm_mode = True


# ---- LISTING IMAGES ----
class ListingImageBase(BaseModel):
    image_url: str
    image_order: int

class ListingImageCreate(ListingImageBase):
    pass

class ListingImage(ListingImageBase):
    listing_image_id: str
    class Config:
        orm_mode = True


# ---- LISTINGS ----
class ListingBase(BaseModel):
    perfume_id: int
    price: float
    condition: Optional[str]
    description: Optional[str]
    type: str

class ListingCreate(ListingBase):
    seller_id: str

class Listing(ListingBase):
    listing_id: str
    status: str
    created_at: datetime
    updated_at: datetime
    images: List[ListingImage] = []
    class Config:
        orm_mode = True