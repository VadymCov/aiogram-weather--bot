import asyncio 
from aiogram import Bot # this is a class for communicating with the Telegram API
from aiogram import Dispatcher # this component that links incoming updates and handlers.
from aiogram.types import Message
from aiogram.filters import CommandStart
from config import YOUR_TOKEN # Important: config.py is added to .gitignore to prevent token leakage.  


bot = Bot(token = YOUR_TOKEN,)
dp = Dispatcher()


@dp.message(CommandStart)
async def start_handler(message:Message):
    await message.answer("Hello i`m bot weather")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())