from sqlalchemy.orm import Session
from app.models.models_disease import Disease


def create_disease(db: Session, disease):
    db_disease = Disease(**disease.model_dump())
    db.add(db_disease)
    db.commit()
    db.refresh(db_disease)
    return db_disease


def get_diseases(db: Session):
    return db.query(Disease).all()


def update_disease(db: Session, disease_id: str, disease_data):
    disease = db.query(Disease).filter(Disease.id == disease_id).first()

    if not disease:
        return None

    for key, value in disease_data.model_dump(exclude_unset=True).items():
        setattr(disease, key, value)

    db.commit()
    db.refresh(disease)
    return disease


def delete_disease(db: Session, disease_id: str):
    disease = db.query(Disease).filter(Disease.id == disease_id).first()

    if not disease:
        return None

    db.delete(disease)
    db.commit()
    return disease