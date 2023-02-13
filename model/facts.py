""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash


'''Class Setup '''

    # Defining the NFLNews class to manage actions in the 'news' table

class FactDay(db.Model):
    __tablename__ = 'Facts'  

    # Defining the Object Variable

    id = db.Column(db.Integer, primary_key=True)
    _date = db.Column(db.String(255), unique=False, nullable=False)
    _fact = db.Column(db.String(255), unique=True, nullable=False)
    
    

    # Constructor of a NFLTeam object, initializes the instance variables within object (self)

    def __init__(self, date, fact):
        self._date = date
        self._fact = fact   # variables with "own"" prefix become part of the object
  

    """Setter and Getter Methods for all Variables"""  

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = data

    @property
    def fact(self):
        return self._fact
    
    @fact.setter
    def fact(self, fact):
        self._fact = fact
    
    
    def __str__(self):
        return json.dumps(self.read())


    """CRUD METHODS """  
    def create(self):
        try:
            db.session.add(self)  
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


    def read(self):
        return {
            "date" : self.date,
            "fact" : self.fact,
        }



"""Database Creation and Testing """

# Builds working data for testing

def initFactDay():
    print("Creating test data")
    """Create database and tables"""
    db.create_all()
    """Tester data for table"""


    f1 = FactDay(date = "February 13th", fact = "The Confederacy approves the recruitment of slaves as soldiers, as long as the approval of their owners is gained.")
    f2 = FactDay(date = "February 14th", fact = "Arizona becomes the 48th state of the union.")
    f3 = FactDay(date = "February 15th", fact = "Canada Maple Leaf Adopted")
    f4 = FactDay(date = "February 16th", fact = "US First 911 Emergency Telephone Service")
    
    factsofficial = [f1, f2, f3, f4]
    
    
    """Builds sample user/note(s) data"""
      for date in factsofficial:
          try:
              date.create()
          except IntegrityError:
              '''fails with bad or duplicate data'''
              db.session.remove()
              print(f"Records exist, duplicate email, or error: {date.uid}")

initFactDay()
