from pathlib import Path

from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import crud, schemas, models
from database import SessionLocal, engine

app = FastAPI(title="ScentTrade API")

app.mount("/static", StaticFiles(directory="static"), name="static")

AUTH_PAGE_PATH = Path("templates/auth.html")

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---- AUTH PAGES ----
@app.get("/auth", response_class=HTMLResponse)
def auth_page():
    """Serve the combined sign-in/sign-up experience."""

    return HTMLResponse(AUTH_PAGE_PATH.read_text(encoding="utf-8"))

# ---- USERS ----
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# ---- BRANDS ----
@app.post("/brands/", response_model=schemas.Brand)
def create_brand(brand: schemas.BrandCreate, db: Session = Depends(get_db)):
    return crud.create_brand(db=db, brand=brand)

# ---- PERFUMES ----
@app.post("/perfumes/", response_model=schemas.Perfume)
def create_perfume(perfume: schemas.PerfumeCreate, db: Session = Depends(get_db)):
    return crud.create_perfume(db=db, perfume=perfume)

# ---- LISTINGS ----
@app.post("/listings/", response_model=schemas.Listing)
def create_listing(listing: schemas.ListingCreate, db: Session = Depends(get_db)):
    return crud.create_listing(db=db, listing=listing)

# ---- LISTING IMAGES ----
@app.post("/listings/{listing_id}/images", response_model=schemas.ListingImage)
def create_listing_image(listing_id: str, image: schemas.ListingImageCreate, db: Session = Depends(get_db)):
    return crud.create_listing_image(db=db, listing_id=listing_id, image=image)
