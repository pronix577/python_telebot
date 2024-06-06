from peewee import (
    AutoField,
    CharField,
    DateTimeField,
    ForeignKeyField,
    IntegerField,
    Model,
    SqliteDatabase,
    FloatField,
)

from config_data.config import DB_PATH


db = SqliteDatabase(DB_PATH)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    username = CharField()
    first_name = CharField()
    last_name = CharField(null=True)


class Games(BaseModel):
    game_id = CharField()
    time_req = DateTimeField()
    home_team = CharField()
    away_team = CharField()
    title = CharField()
    name_team = CharField()
    price = FloatField()


class History(BaseModel):
    id_req = AutoField()
    user = ForeignKeyField(User, backref="history")
    name_users = CharField()
    time_req = DateTimeField()
    command = CharField()
    res_func = CharField()

    def __str__(self):
        return "{id_req}. {name_users} - {time_req} - {name_func}\nResult: {res_func}".format(
            id_req=self.id_req,
            name_users=self.name_users,
            time_req=self.time_req,
            name_func=self.command,
            res_func=self.res_func,
        )


def create_models():
    db.create_tables(BaseModel.__subclasses__())
