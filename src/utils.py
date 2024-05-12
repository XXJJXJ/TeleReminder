import datetime
import os
import json
from src.constants import *

def get_token_file_name():
    env_value = os.getenv('TOKEN_FILE')
    if env_value:
        return env_value
    return 'test'



def read_list_from_env_variable(env_variable_name):
    env_value = os.getenv(env_variable_name)

    if env_value:
        try:
            # Parse the JSON-encoded string into a Python list
            return list(map(int, env_value.split(",")))
        except json.JSONDecodeError:
            # print(f"Error decoding JSON from {env_variable_name}")
            return []
    else:
        # print(f"Environment variable {env_variable_name} not found")
        return []

def parseDate(deadline):
    dateComponents = deadline.split("/")
    day = int(dateComponents[0])
    month = int(dateComponents[1])
    year = int(dateComponents[2])
    return datetime.date(year, month, day)

def get_date_from_firestore(dateString):
    components = str(dateString).split(" ")[0].split("-")
    year = int(components[0])
    month = int(components[1])
    day = int(components[2])
    return datetime.date(year, month, day)


def days_difference(end_date, start_date=datetime.datetime.now()):
    env_val_list = read_list_from_env_variable(UTC_TIMEZONE_DIFF)
    if env_val_list:
        start_date += datetime.timedelta(hours=env_val_list[0])
    start = start_date.date()
    delta = end_date - start
    return delta.days

def get_month(num) -> str:
    m = {
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec',
    }
    return m[num]