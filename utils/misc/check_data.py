import datetime

from database.models import Games
from utils.misc.write_db import writing_to_db


def check_request_data():
    try:
        first_date = Games.select().order_by(Games.time_req).limit(1).get()
        time_diff = datetime.datetime.now() - first_date.time_req
        if time_diff >= datetime.timedelta(hours=1):
            var = Games.delete()
            var.execute()
            writing_to_db()
    except:
        var = Games.delete()
        var.execute()
        writing_to_db()
