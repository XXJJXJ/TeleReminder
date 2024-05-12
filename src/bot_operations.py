import src.database as database
import src.debug as debug

from src.constants import *
from src.utils import *


def exec_save(input, group_id, isAdmin=False):
    try:
        if not isAdmin:
            inputs = input.split(" ", 1)
            date = parseDate(inputs[0])
            if days_difference(date) < 0:
                return
            event_name = inputs[1]
            database.add_event(event_name, date, group_id)
        else:
            inputs = input.split(" ", 2)
            group_name = inputs[0]
            date = parseDate(inputs[1])
            event_name = inputs[2]
            if days_difference(date) < 0:
                return
            for id in database.get_all_groups():
                if id.split(ID_DELIMITER)[0] == group_name:
                    database.add_event(event_name, date, id)
    except Exception as e:
        debug.log(f"Failed to exec_save for group_id: {group_id}, Input", input)
        debug.log("Exec Add Error:", e)

def exec_delete(input, group_id, isAdmin=False):
    try:
        if not isAdmin:
            inputs = input.split(" ", 1)
            date = parseDate(inputs[0])
            database.delete_event(inputs[1], date, group_id)
        else:
            inputs = input.split(" ", 2)
            group_name = inputs[0]
            date = parseDate(inputs[1])
            event_name = inputs[2]
            for id in database.get_all_groups():
                if id.split(ID_DELIMITER)[0] == group_name:
                    database.delete_event(event_name, date, id)
    except Exception as e:
        debug.log(f"Failed to exec_delete for group_id: {group_id}, Input:", input)
        debug.log("Exec Delete Error:", e)

        
async def send_daily_reminder(bot, days_before_to_remind):
    for group_id in database.get_all_groups():
        # debug.log("Sending messages to", group_id)
        chat_id = group_id.split(ID_DELIMITER)[1]
        events = database.get_events(group_id, days_before_to_remind)
        # clear DB for events before and on this date (except for birthdays?)
        database.clear_outdated_events(group_id)
        if events:
            msg = "\n".join(events)
            msg = "Hi everyone! Just a friendly reminder!\n" + msg
            # TODO: Help hyperlink (github readme.md) at the end of the message
            try:
                await bot.send_message(chat_id, msg)
            except Exception as e:
                debug.log(f"Failed to send message to {group_id} because {e}")