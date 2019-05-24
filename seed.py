"""Program for reading a CSV file into the Sasquatch DB"""

import datetime

from model import User, Sightings, connect_to_db, db
from sqlalchemy import update, func
from server import app


def read_in_sighting_data(path1, path2):
    """Reads in csv file without description and location description data"""

    path2_lines = [line.strip("\n") for line in open(path2)]

    for index, row in enumerate(open(path1)):
        row = row.strip().split(",")
        desc_row = path2_lines[index]

        if desc_row[0].isalpha():
            description = desc_row[:-2]
        else:
            description = desc_row[1:-3]

        if not description.endswith("."):
            description += "."

        lat, lng, date = row

        if lat == "":
            lat = None

        if lng == "":
            lng = None

        if date:
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        else:
            date = None

        sighting = Sightings(lat=lat,
                            lng=lng,
                            date=date,
                            event_desc=description)

        db.session.add(sighting)
    
    db.session.commit()


def set_val_sighting_id():
    """Set value for the next user_id after seeding database"""

    # Get the Max user_id in the database
    result = db.session.query(func.max(Sightings.sighting_id)).one()
    max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "select setval('sightings_sighting_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    path1 = "data/bf-lat-long-date.csv"
    path2 = "data/bf-descriptions.csv"

    read_in_sighting_data(path1, path2)
    set_val_sighting_id()

    print("Database seeded")