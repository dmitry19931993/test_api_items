import sqlalchemy
from .base import metadata


products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("price", sqlalchemy.Integer),
    sqlalchemy.Column("status", sqlalchemy.Boolean)
)


