from aiogram.utils.exceptions import NetworkError
from asyncio import sleep


async def send_photo(bot, message_id, path):
    try:
        with open(path, 'rb') as img:
            await bot.send_photo(chat_id=message_id, photo=img)
    except Exception as e:
        print(e)


async def send_mes(bot, message_id, text):
    try:
        await bot.send_message(chat_id=message_id, text=text)
    except Exception as e:
        print(e)
        await sleep(10)
        await bot.send_message(chat_id=message_id, text=text)


