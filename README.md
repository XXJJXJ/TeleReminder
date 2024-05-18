# Introduction
This is a general purpose reminder script that triggers a series of operations to wake up a telegram bot daily and send out reminders based on a configurable number of days away from an event/task.

It utilizes Firebase - Firestore as database to store/keep track of events across different executions and clears the event from the database when the event is passed.


## Tech stack involved
1. Telegram bot api [Link](https://github.com/python-telegram-bot/python-telegram-bot)
2. Firebase - Firestore [Link](https://firebase.google.com/docs/firestore/quickstart)
3. AWS Lambda [Link](https://aws.amazon.com/pm/lambda)
4. AWS EventBridge Scheduler [Link](https://aws.amazon.com/blogs/compute/introducing-amazon-eventbridge-scheduler/)
    - To run the Lambda function regularly
5. Python Programming Language
