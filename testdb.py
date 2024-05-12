from src.database import *
from datetime import date
import lambda_function

TESTING_GROUP_ID = "Bot Testing" + ID_DELIMITER + "-1001581195652"
TESTING_GROUP_ID2 = "Bot test2" + ID_DELIMITER + "-1002132139880"

def test():
    today = date.today()
    three_days_later = today + datetime.timedelta(days=3)
    one_day_later = today + datetime.timedelta(days=1)
    print(days_difference(one_day_later))
    # add_event("Testing yxj", today, TESTING_GROUP_ID)
    # add_event("Testing yxj2", three_days_later, TESTING_GROUP_ID)
    # add_event("Testing yxj1", one_day_later, TESTING_GROUP_ID)
    # add_event("Testing yxj", today, TESTING_GROUP_ID2)
    # add_event("Testing yxj2", three_days_later, TESTING_GROUP_ID2)
    # add_event("Testing yxj1", one_day_later, TESTING_GROUP_ID2)

    # delete_event("Testing yxj", today, TESTING_GROUP_ID)
    # delete_event("Testing yxj2", three_days_later, TESTING_GROUP_ID)
    # delete_event("Testing yxj1", one_day_later, TESTING_GROUP_ID)
    # delete_event("Testing yxj", today, TESTING_GROUP_ID2)
    # delete_event("Testing yxj2", three_days_later, TESTING_GROUP_ID2)
    # delete_event("Testing yxj1", one_day_later, TESTING_GROUP_ID2)

    # freq = set()
    # for i in range(0, 366):
    #     freq.add(i)
    # for e in get_events(TESTING_GROUP_ID2, freq):
    #     print(e)
    

test()