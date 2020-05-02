# python-repository

Implementation of repository in python with SQLAlchemy e sqlite.

### Pre-requisites
* sqlite

### Setup

    $ pip install -r requirements.txt
    $ alembic upgrade head
    $ sqlite3 repo-adventures.db < migrations/data.sql

### Run

    $ python app.py
