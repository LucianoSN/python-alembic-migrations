## Migrations using Alembic with SQL Alchemy

A test project using migrations on SQL Alchemy.

#### Start by installing the module
$ pip install alembic

#### Create your migrations environment. We use "generic" which is a single database setup
$ alembic init --template generic ./migrations

#### Edit alembic.ini with your connection details
$ vim alembic.ini

You can check the current connection using: 

$ alembic current

#### Create first migration

$ alembic revision -m "Create users table"

#### Run our migration and create a table

$ alembic upgrade head

#### Run our migration and create a table

$ alembic downgrade base 

OR 

$ alembic downgrade -1

#### Add exist model using autogenerate

alembic revision --autogenerate -m "Added User model"