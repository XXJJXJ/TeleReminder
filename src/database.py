from datetime import date
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

from src.constants import *
from src.utils import *

cred = credentials.Certificate(f"{get_token_file_name()}_firebase.json")
firebase_admin.initialize_app(cred)
database = firestore.client().collection("UNUSED")


def get_all_groups():
    docs = database.get()
    resp = []
    for d in docs:
        resp.append(d.to_dict()[NAME_FIELD])
    return resp


def get_events(group_id,
                reminders,
                months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                today=date.today()):
    toRemind = []
    for mon in months:
        events_in_month = database.document(group_id).collection(mon).get()
        sorted_events = sorted(events_in_month, key=lambda x:x.to_dict()[DATE_FIELD])
        for d in sorted_events:
            data = d.to_dict()
            # parse time
            date = get_date_from_firestore(data[DATE_FIELD])
            days_away = days_difference(date)
            if days_away in reminders:
                if days_away == 0:
                    toRemind.append(f'{data[NAME_FIELD]} today!')
                elif days_away == 1:
                    toRemind.append(f'{data[NAME_FIELD]} in a day!')
                else:
                    toRemind.append(f'{data[NAME_FIELD]} in {days_away} days time!')
    return toRemind


def clear_outdated_events(group_id):
    today = date.today()
    month = get_month(today.month)
    events = database.document(group_id).collection(month).get()
    for e in events:
        data = e.to_dict()
        event_date = get_date_from_firestore(data[DATE_FIELD])
        if days_difference(event_date) <= 0:
            delete_event(data[NAME_FIELD], event_date, group_id)


def add_event(event_name, event_date: datetime, group_id):
    if days_difference(event_date) < 0:
        return
    month = get_month(event_date.month)
    # To be able to identify the group
    database.document(group_id).set({
        NAME_FIELD: group_id,
    })
    # Overwrites if exist
    database.document(group_id).collection(month).document(event_name).set({
        NAME_FIELD: event_name,
        # need to convert datetime.date to datetime.datetime (below)
        DATE_FIELD: datetime.datetime.combine(event_date, datetime.time.min),
    })


def delete_event(event_name, event_date: datetime, group_id):
    month = get_month(event_date.month)
    doc = database.document(group_id).collection(month).document(event_name).get()
    if doc.exists:
        database.document(group_id).collection(month).document(event_name).delete()