import random
import string

import pytz
import time
from datetime import datetime

# import dateutil.relativedelta
# from dateutil import tz
# import phonenumbers
# from phonenumbers import carrier
# from phonenumbers.phonenumberutil import number_type
# import dateutil.parser
# from hashids import Hashids


def now_timestamp():
    return round(time.time())


def get_datetime_timezone(timestamp, timezone="Asia/Ho_Chi_Minh"):
    return datetime.fromtimestamp(timestamp / 1000, tz=pytz.timezone(timezone))


# GET BY TIMEZONE


def get_datetime_now(timezone="Asia/Ho_Chi_Minh"):
    return datetime.now(tz=pytz.timezone(timezone))


# GET BY GMT +7


# def get_local_today(timezone=7):
#     today = datetime.utcnow() + dateutil.relativedelta.relativedelta(hours=timezone)
#     return today


# def timestamp_to_string(datetime, out_format="%d/%m/%Y %H:%M"):
#     new_time_zone = get_datetime_timezone(datetime)
#     try:
#         date_time = new_time_zone.strftime(out_format)
#     except:
#         date_time = new_time_zone.strftime("%d/%m/%Y %H:%M")
#     return date_time


def get_year_later(number_of_year):
    udate_now = datetime.utcnow()
    current_year = udate_now.year
    date = udate_now.replace(year=current_year + number_of_year)
    return date


def get_start_time_of_day(timestamp=None, timezone="Asia/Ho_Chi_Minh"):
    if timestamp is None:
        timestamp = now_timestamp()
    date = datetime.fromtimestamp(timestamp / 1000, tz=pytz.timezone(timezone))
    start_time_date = date.replace(hour=0, minute=0, second=0, microsecond=0)
    return start_time_date


def get_end_time_of_day(timestamp=None, timezone="Asia/Ho_Chi_Minh"):
    if timestamp is None:
        timestamp = now_timestamp()
    date = datetime.fromtimestamp(timestamp / 1000, tz=pytz.timezone(timezone))
    end_time_date = date.replace(hour=23, minute=59, second=59, microsecond=999)
    return end_time_date


# change phone format
def convert_phone_number(phone, output_type="0"):
    tmp_phone = str(phone)
    output_type = str(output_type)

    tmp_phone = tmp_phone.replace(" ", "")
    if len(tmp_phone) < 13 and len(tmp_phone) > 9:
        if output_type == "84":
            if tmp_phone.startswith("84"):
                pass
            elif tmp_phone.startswith("0"):
                tmp_phone = tmp_phone.replace("0", "84", 1)
            elif tmp_phone.startswith("+84"):
                tmp_phone = tmp_phone.replace("+84", "84", 1)
            else:
                return None
            return tmp_phone

        elif output_type == "+84":
            if tmp_phone.startswith("+84"):
                pass
            elif tmp_phone.startswith("0"):
                tmp_phone = tmp_phone.replace("0", "+84", 1)
            elif tmp_phone.startswith("84"):
                tmp_phone = tmp_phone.replace("84", "+84", 1)
            else:
                return None
            return tmp_phone
        else:
            if tmp_phone.startswith("0"):
                pass
            elif tmp_phone.startswith("84"):
                tmp_phone = tmp_phone.replace("84", "0", 1)
            elif tmp_phone.startswith("+84"):
                tmp_phone = tmp_phone.replace("+84", "0", 1)
            else:
                return None
            return tmp_phone
    elif len(tmp_phone) == 9:
        tmp_phone = "0" + tmp_phone
        return tmp_phone
    else:
        return None


# def convert_datetime_format(input_datetime, outFormat=None):
#     try:
#         find_input_date = date_detector(input_datetime)

#         if find_input_date is not None:
#             if outFormat == None:
#                 outFormat = "%d/%m/%Y %H:%M:%S"

#             return find_input_date.__format__(outFormat)

#         return None
#     except:
#         return None


def generate_random_string(length: int):
    # choose from all lowercase letter
    letters = string.ascii_lowercase + string.digits
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str
