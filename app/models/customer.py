from flask import current_app
from app import db
from datetime import datetime
from sqlalchemy.orm import backref, relationship

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    postal_code = db.Column(db.String)
    phone = db.Column(db.String)
    registered_at = db.Column(db.DateTime, nullable = True)
    videos_checked_out_count = db.Column(db.Integer, default = 0) 

    # One to many relationship: one customer has many rentals 
    customers = db.relationship("Rental", backref="customers", lazy=True)


    def to_json(self):
        return {
            "id": self.customer_id,
            "name": self.name,
            "registered_at": self.registered_at,
            "postal_code": self.postal_code,
            "phone":self.phone,
            "videos_checked_out_count":self.videos_checked_out_count
            }   
            # this changes to len (self.rentals) for the relationship 