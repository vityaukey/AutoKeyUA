from services.key_database import KeyDatabase


db = KeyDatabase()

keys = db.search("Skoda")


for key in keys:
    print(key)