import datetime

from database.models import History


def log_request(user_id, name_user, commands, result):
    History.create(
        user=user_id,
        name_users=name_user,
        time_req=datetime.datetime.now(),
        command=commands,
        res_func=result,
    )
