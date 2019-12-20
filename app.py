from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'

db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), unique=False)
    lastname = db.Column(db.String(100), unique=False)
    street = db.Column(db.String(100), unique=False)
    city = db.Column(db.String(100), unique=False)
    state = db.Column(db.String(2), unique=False)
    zipcode = db.Column(db.String(5), unique=False)
    policies = db.relationship('Policy', backref='contact', lazy=True)

    def __repr__(self):
        return '<Contact for: %r>' % self.firstname


class Policy(db.Model):
    policy_number = db.Column(db.Integer, primary_key=True)
    policy_type = db.Column(db.String(100), unique=True, nullable=False)
    effective_date = db.Column(db.DateTime)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'), nullable=False)

    def __repr__(self):
        return '<Policy type: %r>' % self.policy_type


db.create_all()


@app.route('/')
def check():
    return request.remote_addr


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
