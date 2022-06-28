from datetime import datetime
import pytz


def calc_time_return_dict(timezone_str):
    tz = pytz.timezone(timezone_str)
    dt = datetime.now(tz)
    dict_time = {
        'year': dt.year,
        'month': dt.month,
        'day': dt.day,
        'hour': dt.hour,
        'minute': dt.minute,
        'second': dt.second,
    }
    return dict_time
