from .db import db


class Property(db.Model):
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey("states.id"), nullable=False)
    zipcode = db.Column(db.String(5), nullable=False)
    homeStatus = db.Column(db.String(20))
    homeType = db.Column(db.String(20))
    bed = db.Column(db.Integer)
    bath = db.Column(db.Float)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    imageURI = db.Column(db.String)
    unit = db.Column(db.String)
    price = db.Column(db.Float)
    livingArea = db.Column(db.Float)
    lotAreaValue = db.Column(db.Float)
    lotAreaUnit = db.Column(db.String(20))
    zestimate = db.Column(db.Float)
    rentZestimate = db.Column(db.Float)
    zpid = db.Column(db.Integer)
    daysOnZillow = db.Column(db.Integer)

    state = db.relationship("State", back_populates="properties")
