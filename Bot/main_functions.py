import secondary_functions as sf
from Screenshot import Screenshot
from JSONFile import JSONFile
from config import PATH_SCHEDULE_SCREENSHOT, PATH_SCREENSHOT


async def process(bot, message_id, n):
    file = JSONFile()
    if message_id not in await file.get_all_users():
        text = "Вы не в списке разрешенных пользователей." if n else \
            "Пожалуйста, введите команду /start для корректной работы бота."
    else:
        await file.get_new_data(message_id, n)
        text = "Бот запущен." if n else "Бот остановлен."
    await sf.send_mes(bot, message_id, text)


async def send_screenshot(bot, message_id):
    desktop = Screenshot(PATH_SCREENSHOT)
    file = JSONFile()
    await desktop.get_screenshot()
    if message_id not in await file.get_all_users():
        await sf.send_mes(bot, message_id, "Вы не в списке разрешенных пользователей.")
    else:
        await sf.send_photo(bot, message_id, desktop.path)


async def do_screenshots(bot):
    desktop = Screenshot(PATH_SCHEDULE_SCREENSHOT)
    file = JSONFile()
    if await desktop.process_screenshot():
        for chat in await file.get_work_users():
            await sf.send_photo(bot, chat, desktop.path)
            await sf.send_mes(bot, chat, "Возможно, вы погибли.")

