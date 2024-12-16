import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher

from database.db.base import init_models
from handlers import main_menu
from loguru import logger
from dotenv import load_dotenv

load_dotenv()


async def db_init_models():
    await init_models()
    logger.info("База данных инициализирована")


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=os.environ.get("BOT_TOKEN"))
    dp = Dispatcher()
    logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")
    dp.include_routers(main_menu.router)
    logger.info("Роутеры подключены")
    # await db_init_models()
    await bot.delete_webhook(drop_pending_updates=True)         # закомментировать на проде
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())