import asyncio 
import aiohttp ##
from aiogram import Bot # this is a class for communicating with the Telegram API
from aiogram import Dispatcher  # this component that links incoming updates and handlers.
from aiogram.types import Message
from aiogram.filters import Command
from config import YOUR_TOKEN # Important: config.py is added to .gitignore to prevent token leakage.  
from config import WEATHER_API_KEY # Important: config.py is added to .gitignore to prevent API-KEY leakage.

bot = Bot(token = YOUR_TOKEN,)
dp = Dispatcher()

async def get_weather(city: str)->str:
    url = (
        "http://api.openweathermap.org/data/2.5/weather"
    f"?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=en"
    )
    async with aiohttp.ClientSession() as session: # creates a session for HTTP requests
        async with session.get(url) as response: # sends a GET request
            data = await response.json() # waits for a response and turns it into a Python dictionary
    if response.status != 200:
        return '📛error name'
    descr = data["weather"][0]["description"].capitalize() # first element of the weather array
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    return f"Weather☀\nCity: {city.title()}:\n{descr}: {temp}°c (Feels like {feels_like})" # display the weather beautifully on the screen

@dp.message(Command("start")) 
async def start_handler(message:Message):
    await message.answer(f"Hello, {message.from_user.first_name} 🖐\ni`m bot weather.\nEnter the name of the city.")


@dp.message()
async def handler_city_name(message:Message): # Function handler of plain text and sending to get_weather
    city = message.text
    weather_info = await get_weather(city)
    await message.reply(weather_info)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())