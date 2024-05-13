# Introduction
This is a general purpose reminder script that triggers a series of operations to wake up a telegram bot daily and send out reminders based on a configurable number of days away from an event/task.

It utilizes Firebase - Firestore as database to store/keep track of events across different executions and clears the event from the database when the event is passed.


## Tech stack involved
1. Telegram bot api [Link]()
2. Firebase - Firestore [Link]()
3. AWS EventBridge (For scheduled running) [Link]()
4. Python Programming Language
