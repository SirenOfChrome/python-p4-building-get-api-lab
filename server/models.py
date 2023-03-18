from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakery'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)

    baked_goods = db.relationship("BakedGood", backref="bakery", lazy=True)

    serialize_only = ('id', 'name', 'created_at', 'updated_at', 'baked_goods')

class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_good'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakery.id'), nullable=False)

    bakery = db.relationship("Bakery", back_populates="baked_goods")

    serialize_only = ('id', 'name', 'price', 'created_at', 'updated_at', 'bakery_id', 'bakery')

    
