from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import asyncio
import aioschedule
import main_functions as mf
from config import INTERVAL_TIME
import os
from dotenv import load_dotenv


load_dotenv()
bot = Bot(token=os.environ['TOKEN'])
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


async def on_startup(_):
    asyncio.create_task(scheduler())


@dp.message_handler(commands='start')
async def process_start(message: types.Message):
    await mf.process(bot, message.chat.id, 1)
    await message.delete()


@dp.message_handler(commands='finish')
async def process_finish(message: types.Message):
    await mf.process(bot, message.chat.id, 0)
    await message.delete()


@dp.message_handler(commands='screenshot')
async def process_screenshot(message: types.Message):
    await mf.send_screenshot(bot, message.chat.id)
    await message.delete()


async def scheduler():
    aioschedule.every(INTERVAL_TIME).minutes.do(mf.do_screenshots, bot)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


