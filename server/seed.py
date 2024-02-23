#!/usr/bin/env python3

from app import app
from models import db, Truck # models go here
from faker import Faker

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        print("Clearing old trucks")

        Truck.query.delete()

        # write your seeds here!
        print("Making trucks!")

        t1 = Truck(name=faker.name(), location = faker.country(), model = "Frieghtliner", insurance = "23,232" )
        t2 = Truck(name=faker.name(), location = faker.country(), model = "Peterbilt", insurance = "42,234")
        t3 = Truck(name=faker.name(), location = faker.country(), model = "Volov", insurance = "32,969")



        db.session.add_all ([ t1,t2,t3 ])
        db.session.commit()

        print("Seeding complete!")
