from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from datetime import datetime


app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'

app.secret_key = 'dev'
app.config.from_pyfile('config.py', silent=True)


db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), unique=True, nullable=False)
    lastname = db.Column(db.String(100), unique=True, nullable=False)
    street = db.Column(db.String(100), unique=True, nullable=False)
    city = db.Column(db.String(100), unique=True, nullable=False)
    state = db.Column(db.String(2), unique=True, nullable=False)
    zipcode = db.Column(db.String(5), unique=True, nullable=False)
    policies = db.relationship('Policy', backref='contact', lazy=True)

    def __repr__(self):
        return '<Contact for: %r %r>' % (self.firstname, self.lastname)


class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    policy_number = db.Column(db.String(100), unique=True, nullable=False)
    policy_type = db.Column(db.String(100), unique=True, nullable=False)
    effective_date = db.Column(db.DateTime, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact.id'),
                           nullable=False)

    def __repr__(self):
        return '<Policy type: %r>' % self.policy_type


db.create_all()

admin = Admin(app)

admin.add_view(ModelView(Policy, db.session))
admin.add_view(ModelView(Contact, db.session))


@app.route('/')
def check():
    return request.remote_addr


if __name__ == "__main__":
    app.run(host="0.0.0.0")
