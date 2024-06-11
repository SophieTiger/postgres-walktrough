from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Programmer" table
# class Programmer(base):
#     __tablename__ = "Programmer"
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     gender = Column(String)
#     nationality = Column(String)
#     famous_for = Column(String)

# create a class-based model for the "Countries" table
class Countries(base):
    __tablename__ = "Countries"
    id = Column(Integer, primary_key=True)
    country_name = Column(String)
    language = Column(String)
    climate = Column(String)
    best_food = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Programmer table
# ada_lovelace = Programmer(
#     first_name = "Ada",
#     last_name = "Lovelace",
#     gender = "F",
#     nationality = "British",
#     famous_for = "First Programmer"
# )

# alan_turing = Programmer(
#     first_name = "Alan",
#     last_name = "Turing",
#     gender = "M",
#     nationality = "British",
#     famous_for = "Modern Computing"
# )

# grace_hopper = Programmer(
#     first_name = "Grace",
#     last_name = "Hopper",
#     gender = "F",
#     nationality = "American",
#     famous_for = "COBOl language"
# )

# margaret_hamilton = Programmer(
#     first_name = "Margaret",
#     last_name = "Hamilton",
#     gender = "F",
#     nationality = "American",
#     famous_for = "Software Engineering"
# )

# bill_gates = Programmer(
#     first_name = "Bill",
#     last_name = "Gates",
#     gender = "M",
#     nationality = "American",
#     famous_for = "Microsoft"
# )

# tim_berners_lee = Programmer(
#     first_name = "Tim",
#     last_name = "berners-Lee",
#     gender = "M",
#     nationality = "British",
#     famous_for = "World Wide Web"
# )

# sophie_tigerholm = Programmer(
#     first_name = "Sophie",
#     last_name = "Tigerholm",
#     gender = "F",
#     nationality = "Swedish",
#     famous_for = "Problem Solving"
# )

# creating records on our Countries table
thailand = Countries(
    country_name = "Thailand",
    language = "Thai",
    climate = "Tropical",
    best_food = "Kao Soi"
)

sweden = Countries(
    country_name = "Sweden",
    language = "Swedish",
    climate = "Arctic",
    best_food = "Meatballs"
)

india = Countries(
    country_name = "India",
    language = "Multiple",
    climate = "Tropical",
    best_food = "Garam Masala"
)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(sophie_tigerholm)
# session.add(thailand)
# session.add(sweden)
# session.add(india)

# commit our session to the database
# session.commit()


# updating a single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "World President"

# commit our session to the database
# session.commit()

# updating a single record
country = session.query(Countries).filter_by(id=12).first()
country.best_food = "Tikka Masala"

# commit our session to the database
session.commit()


# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# defensive programming
# if programmer is not None:
#     print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")

# deleting a single record
land = input("Enter a country: ")
country = session.query(Countries).filter_by(country_name=land).first()
# defensive programming
if country is not None:
    print("Country found: ", country.country_name)
    confirmation = input("Are you sure you want to delete this record? (y/n) ")
    if confirmation.lower() == "y":
        session.delete(country)
        session.commit()
        print("Country has been deleted")
    else:
        print("Country not deleted")
else:
    print("No records found")

# query the database to find all Programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + " " + programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         programmer.famous_for,
#         sep=" | "
#     )

# query the database to find all Countries
countries = session.query(Countries)
for country in countries:
    print(
        country.id,
        country.country_name,
        country.language,
        country.climate,
        country.best_food,
        sep=" | "
    )