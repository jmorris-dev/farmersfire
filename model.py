from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////db.db'
db = SQLAlchemy(app)


class Policy(db.Model):
    policy_number = db.Column(db.Integer, primary_key=True)
    policy_type = db.Column(db.String(100), unique=True, nullable=False)
    effective_date = db.Column(db.DateTime.date)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'), nullable=False)

    def __repr__(self):
        return '<Policy type: %r>' % self.policy_type


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), unique=False, nullable=False)
    lastname = db.Column(db.String(100), unique=False, nullable=False)
    street = db.Column(db.String(100), unique=False, nullable=False)
    city = db.Column(db.String(100), unique=False, nullable=False)
    state = db.Column(db.String(2), unique=False, nullable=False)
    zipcode = db.Column(db.String(5), unique=False, nullable=False)
    policies = db.relationship('Policy', backref='contact')

    def __repr__(self):
        return '<Contact for: %r %r>' % self.firstname, self.lastname


db.create_all()
