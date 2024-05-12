import telegram
import src.debug as debug
import src.bot_operations as bot_operations
from src.constants import *
from src.utils import *

async def run_bot_routine():
    TOKEN_FILENAME = f'{get_token_file_name()}_token'
    TOKEN = open(TOKEN_FILENAME, "r").read()
    bot = telegram.Bot(TOKEN)
    # READ in remind frequency from Env Variable (if any)
    freq = read_list_from_env_variable(REMIND_FREQUENCY_ENV_VAR)
    days_before_to_remind = set(freq)
    if len(days_before_to_remind) == 0:
        # default
        days_before_to_remind = {3, 1, 0}
    # debug.log("Reminder frequency is:", days_before_to_remind, "days")
    # debug.log("Today's date:", today)

    async with bot:
        updates = (await bot.get_updates(allowed_updates=["message"]))
        for u in updates:
            if not u.message or not u.message.text or not u.message.chat_id:
                # some special updates dont have text/chat_id field
                continue
            # debug.log(u)
            chat_id = u.message.chat_id
            group_name = u.message.chat.title
            group_id = group_name + ID_DELIMITER + str(chat_id)
            if u.message.text.startswith(SAVE) or u.message.text.startswith(DELETE):
                lines = u.message.text.split("\n")
                for line in lines:
                    if line.startswith(SAVE):
                        bot_operations.exec_save(line.removeprefix(SAVE), group_id)
                    elif line.startswith(DELETE):
                        bot_operations.exec_delete(line.removeprefix(DELETE), group_id)
            elif u.message.text.startswith(ADMIN_SAVE) or u.message.text.startswith(ADMIN_DELETE):
                lines = u.message.text.split("\n")
                # for line in lines:
                    # if line.startswith(ADMIN_SAVE):
                    #     bot_operations.exec_save(line.removeprefix(SAVE), group_id, True)
                    # elif line.startswith(ADMIN_DELETE):
                    #     bot_operations.exec_delete(line.removeprefix(DELETE), group_id, True)

        await bot_operations.send_daily_reminder(bot, days_before_to_remind)

# if __name__ ==  '__main__':
#     asyncio.run(run_bot_routine())