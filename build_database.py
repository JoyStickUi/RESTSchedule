from config import db

# Create the database
db.create_all()

db.session.commit()
