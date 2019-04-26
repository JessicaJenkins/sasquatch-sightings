"""Program for reading a CSV file into the Sasquatch DB"""

import datetime

from model import User, Sightings, connect_to_db, db
from sqlalchemy import update
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
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
        else:
            date = None

        sighting = Sightings(lat=lat,
                            lng=lng,
                            date=date,
                            event_desc=description)

        db.session.add(sighting)
    
    db.session.commit()


# def read_in_description(description_file):
#     """Reads in description data for corresponding sightings"""

#     for i, row in enumerate(open(description_file)):
#         if row[0].isalpha():
#             description = row[:-2]
#         else:
#             description = row[1:-3]

#         if not description.endswith("."):
#             description += "."

#         db.session.update(sightings).where(sightings.sighting_id==i).values(event_desc=description)



if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()