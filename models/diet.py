from database import db
from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import mapped_column

class Diet(db.Model):
  __tablename__ = 'diets'

  id = mapped_column(String(14), primary_key=True)
  name = mapped_column(String(80), unique=True)
  description = mapped_column(String(120))
  date = mapped_column(DateTime, nullable=False)
  is_diet = mapped_column(Boolean, default=False)

def create_diet_db(diet: Diet):
  try:
    db.session.add(diet)
    db.session.commit()
    return True
  except:
    db.session.rollback()
    return False

def get_diets_db(id: str):
  try:
    diet = Diet.query.get(id)
    return diet
  except:
    return None

def get_all_diets_db():
  try:
    diets = Diet.query.all()
    return diets
  except:
    return []

def update_diet_db(id: str, diet: Diet):
  try:
    diet_to_update = Diet.query.get(id)

    if diet_to_update:
      diet_to_update.name = diet.name
      diet_to_update.description = diet.description
      diet_to_update.date = diet.date
      diet_to_update.is_diet = diet.is_diet

      db.session.commit()
      return True

    return False
  except:
    db.session.rollback()
    return False

def delete_diet_db(id: str):
  try:
    diet = Diet.query.get(id)

    if diet:
      db.session.delete(diet)
      db.session.commit()
      return True
    
    return False
  except:
    db.session.rollback()
    return False
