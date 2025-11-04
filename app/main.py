from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, models, schemas, auth

app = FastAPI(title="🏋️ Fitness Studio Booking API")

models.Base.metadata.create_all(bind=database.engine)

# Register authentication routes
app.include_router(auth.router, tags=["Auth"])

@app.post("/classes", tags=["Classes"])
def create_class(fitness_class: schemas.ClassCreate, db: Session = Depends(database.get_db), user=Depends(auth.get_current_user)):
    new_class = models.FitnessClass(**fitness_class.dict())
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class

@app.get("/classes", tags=["Classes"])
def get_classes(db: Session = Depends(database.get_db)):
    return db.query(models.FitnessClass).all()

@app.post("/book", tags=["Bookings"])
def book_class(booking: schemas.BookingCreate, db: Session = Depends(database.get_db), user=Depends(auth.get_current_user)):
    fitness_class = db.query(models.FitnessClass).filter(models.FitnessClass.id == booking.class_id).first()
    if not fitness_class:
        raise HTTPException(status_code=404, detail="Class not found")
    if fitness_class.availableSlots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    new_booking = models.Booking(
        user_id=user.id,
        class_id=booking.class_id,
        client_name=booking.client_name,
        client_email=booking.client_email,
    )
    fitness_class.availableSlots -= 1
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return {"message": "Class booked successfully"}

@app.get("/bookings", tags=["Bookings"])
def get_user_bookings(db: Session = Depends(database.get_db), user=Depends(auth.get_current_user)):
    return db.query(models.Booking).filter(models.Booking.user_id == user.id).all()
