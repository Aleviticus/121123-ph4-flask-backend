#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import Truck, db # import your models here!

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

#T TODO: import and add in cors here 
CORS(app)

migrate = Migrate(app, db)

db.init_app(app)

# Routes

@app.get('/')
def index():
    return make_response( jsonify("Hello world") )

@app.post('/')
def post_index():
    data = request.json
    data["location"] = "five guys"
    return make_response( jsonify(data))

@app.get('/trucks')
def get_trucks():
    trucks = Truck.query.all()
    return [ trucks.to_dict() for trucks in trucks ], 200

@app.get('/trucks/<int:id>')
def get_truck_by_(id):
    found_trucks = Truck.query.where(Truck.id == id).first()
    if found_trucks:
     return make_response( jsonify(found_trucks.to_dict()), 200)
    else:
        return { "error": "Not Found"}, 404
    
# PATCH TRUCK BY ID UPDATE TRUCK
    
@app.patch("/trucks/<int:id>")
def update_truck(id):
    data = request.json
    found_truck = Truck.query.where(Truck.id == id).first()

    if found_truck:

        for key in data:
            setattr( found_truck, key, data[key] )
        
        db.session.commit()
        return found_truck.to_dict(), 202
    else:
        return {"error": "Not Found"}, 404
    
# POST TRUCKS - Create Route
    
@app.post('/trucks')
def create_trucks():
    data = request.json

    try:

        new_trucks = Truck(name=data.get('name'), location=data.get("location"), insurance=data.get("insurance"), model=data.get("model"))
        db.session.add( new_trucks )
        db.session.commit()
        return new_trucks.to_dict(), 201
    
    except:
        return { "error": "Invalid truck please try again"}, 405
    
#Delete TRUCKS 
    
@app.delete('/trucks/<int:id>')
def delete_truck(id):
    found_truck = Truck.query.where(Truck.id == id).first()

    if found_truck:

        db.session.delete(found_truck)
        db.session.commit()

        return{}, 204

    else:
        return { "error": "Not Found" }, 404



# write your routes here!

if __name__ == '__main__':
    app.run(port=5555, debug=True)
