from sqlalchemy.orm import Session
import models, schemas

# ---- USERS ----
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ---- BRANDS ----
def create_brand(db: Session, brand: schemas.BrandCreate):
    db_brand = models.Brand(**brand.dict())
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand

# ---- PERFUMES ----
def create_perfume(db: Session, perfume: schemas.PerfumeCreate):
    db_perfume = models.Perfume(**perfume.dict())
    db.add(db_perfume)
    db.commit()
    db.refresh(db_perfume)
    return db_perfume

# ---- LISTINGS ----
def create_listing(db: Session, listing: schemas.ListingCreate):
    db_listing = models.Listing(**listing.dict())
    db.add(db_listing)
    db.commit()
    db.refresh(db_listing)
    return db_listing

# ---- LISTING IMAGES ----
def create_listing_image(db: Session, listing_id: str, image: schemas.ListingImageCreate):
    db_image = models.ListingImage(**image.dict(), listing_id=listing_id)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image