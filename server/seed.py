from faker import Faker
from models import db, Pet
from app import app

faker = Faker()

# Seed script to populate the pets table
with app.app_context():
    print("Clearing pets table...")
    Pet.query.delete()

    print("Adding fake pets...")
    for _ in range(10):
        pet = Pet(
            name=faker.first_name(),
            species=faker.random_element(elements=('Dog', 'Cat', 'Hamster', 'Turtle', 'Chicken'))
        )
        db.session.add(pet)

    db.session.commit()
    print("Seeding complete!")
