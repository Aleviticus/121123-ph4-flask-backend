from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Truck(db.Model):

    __tablename__ = "truck_table"

    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String, unique=True )
    location = db.Column ( db.String )
    model = db.Column ( db.String )
    insurance = db.Column ( db.Integer )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self. model,
            "location": self.location,
            "insurance": self.insurance
        }

# write your models here!
