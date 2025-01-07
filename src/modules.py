"""
Requirements
------------
    pip install sqlalchemy
    pip install mysql-connector-python

db URL general template:
<dialect>+<driver>://<username>:<password>@<hostname>:<port>/<database>"
------------------
    My sql
    mysql_db_url = "mysql://<username>:<password>@<hostname>:<port>/<database>
    mysql_db_url = "mysql+mysqlconnector://<username>:<password>@<hostname>:<port>/<database>

    PostgreSQL
    postgresql_dg_url = "postgresql://<username>:<password>@<hostname>:<port>/<database>"
    "postgresql+psycopg2://<username>:<password>@<hostname>:<port>/<database>"

Get username and port from SQL server
--------------------
    CREATE DATABASE text_docker;
    USE test_docker;

    SHOW VARIABLES WHERE Variable_name = 'port'
    SELECT user();
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the MySQL database URL
mysql_db_url = "mysql+mysqlconnector://root:Changeme_123@localhost:3306/weeding_users"

# Create the SQLAlchemy engine
engine = create_engine(mysql_db_url)

# Create a session maker
Session = sessionmaker(bind=engine)
session = Session()

# Define the base class for ORM models
Base = declarative_base()

class User(Base):
    """
    ORM model representing the 'users' table in the database.

    Attributes:
        id (Integer): Primary key, auto-incremented.
        firstname (String): First name of the user, up to 20 characters.
        lastname (String): Last name of the user, up to 40 characters.
        phone (String): Phone number of the user, up to 20 characters.
        participation (String): Participation status of the user.
        non_participants_details (String): Details for non-participation, up to 400 characters.
        extra_details (String): Any additional details, up to 400 characters.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(40), nullable=False)
    phone = Column(String(20), nullable=False)
    participation = Column(String(20), nullable=False)
    non_participants_details = Column(String(400))
    extra_details = Column(String(400), nullable=True)

# Create all tables in the database
Base.metadata.create_all(engine)
