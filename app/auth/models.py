from . import db
from datetime import datetime, timezone


class Users(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, Unique=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone_number = db.Column(db.String)
    birth_date = db.Column(db.Date)
    gender = db.Column(db.String, db.CheckConstraint("gender IN ('Male', 'Female', 'Prefer not to say')"), nullable=True)
    profile_image = db.Column(db.String(255))
    account_status = db.Column(db.String(20), db.CheckConstraint("account_status IN ('Active', 'Inactive', 'Suspended')"), default='Active')
    role = db.Column(db.String(20), db.CheckConstraint("role IN ('Customer', 'Vendor', 'Admin')"), default='Customer')
    created_at = db.Column(db.TIMESTAMP, default=datetime.now(timezone.utc)) 
    updated_at = db.Column(db.TIMESTAMP, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    last_login = db.Column(db.TIMESTAMP)
    email_verified = db.Column(db.Boolean, default=False)
    phone_verified = db.Column(db.Boolean, default=False)
    reset_token = db.Column(db.String(255))
    
    def __repr__(self):
        return f"User(Name: '{self.username}', Email: '{self.email}')"
