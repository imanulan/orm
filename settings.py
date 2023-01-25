import peewee



db = peewee.PostgresqlDatabase(
    'orm_py25',
    user='hello',
    password='1',
    host='localhost',
    port=5432,
)