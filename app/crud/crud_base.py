class CRUDBase:
    def __init__(self, model):
        self.model = model

    def create(self, db, db_obj):
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_all(self, db, skip: int = 0, limit: int = 10):
        return db.query(self.model).offset(skip).limit(limit).all()

    def get_by_id(self, db, obj_id: str):
        return db.query(self.model).filter(
            self.model.id == obj_id
        ).first()

    def update(self, db, obj_id: str, obj_data):
        db_obj = self.get_by_id(db, obj_id)

        if not db_obj:
            return None

        for key, value in obj_data.model_dump(exclude_unset=True).items():
            setattr(db_obj, key, value)

        db.commit()
        db.refresh(db_obj)

        return db_obj

    def delete(self, db, obj_id: str):
        db_obj = self.get_by_id(db, obj_id)

        if not db_obj:
            return None

        db.delete(db_obj)
        db.commit()

        return db_obj