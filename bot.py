import asyncio 
from aiogram import Bot # this is a class for communicating with the Telegram API
from aiogram import Dispatcher # this component that links incoming updates and handlers.
from config import TOKEN # Important: config.py is added to .gitignore to prevent token leakage.  

bot = Bot(token = TOKEN)
dp = Dispatcher


