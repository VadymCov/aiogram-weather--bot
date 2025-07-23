import asyncio 
import aiohttp ##
from aiogram import Bot # this is a class for communicating with the Telegram API
from aiogram import Dispatcher  # this component that links incoming updates and handlers.
from aiogram.types import Message
from aiogram.filters import CommandStart
from config import YOUR_TOKEN # Important: config.py is added to .gitignore to prevent token leakage.  
from config import WEATHER_API_KEY # Important: config.py is added to .gitignore to prevent API-KEY leakage.

bot = Bot(token = YOUR_TOKEN,)
dp = Dispatcher()

async def get_weather(city: str)->str:
    url = (
        "http://api.openweathermap.org/data/2.5/weather"
    f"?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=eng"
    )
    async with aiohttp.ClientSession() as session: # creates a session for HTTP requests
        async with session.get(url) as response: # sends a GET request
            data = await response.json() # waits for a response and turns it into a Python dictionary
    if response.status != 200:
        return '📛error'
    descr = data["weather"][0]["descriptions"].capitalize() # first element of the weather array
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    return f"weather in {city} - {descr}: '{temp}°c feels like {feels_like}'" # display the weather beautifully on the screen


@dp.message(CommandStart)
async def start_handler(message:Message):
    await message.answer(f"Hello, {message.from_user.first_name}.\ni`m bot weather")



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())