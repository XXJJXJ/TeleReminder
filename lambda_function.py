import asyncio
import json
import src.main

def lambda_handler(event, context):
    asyncio.run(src.main.run_bot_routine())
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda Finished running')
    }
