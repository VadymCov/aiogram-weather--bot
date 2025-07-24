# 🌤️ Telegram weather bot

A simple and fast Telegram bot that provides up-to-date weather information in any city in the world.

![Demo bot](./image/bot_weather.jpg)

## ✨ Features

- 🔍 Find out the weather in any city by simply entering its name.
- 🌡️ Shows the temperature and "feels" like it in degrees Celsius.
- 📝 Provides a description of the weather in English.
- ⚡ Fast asynchronous processing with aiohttp.

## 📋 Example

**Input:** `Moscow`

**Output:**
```
Weather☀
City: Los Angeles:
Clear sky: 15°C (feels like 12)
```

## 🛠️ Tech stack

- **Python 3.7+**
- **aiogram** - Telegram Bot API framework
- **aiohttp** - Asynchronous HTTP client
- **OpenWeatherMap API** - Weather data source

## 📁 Project structure

```
weather-telegram-bot/
├── bot.py # Main bot code
├── config.py # Configuration file (not in repository)
├── image/ # Screenshots and demo images
└── README.md # This file
```

## 🔒 Security

- All sensitive data (tokens, API keys) are stored in `config.py`
- `config.py` is added to `.gitignore` to prevent token leaks
- Never commit your tokens to public repositories

## 🤝 Contribute

1. Fork the repository
2. Create a branch with the new feature (`git checkout -b feature/amazing-feature`)
3. Commit the changes (`git commit -m 'Add amazing feature'`)
4. Push the changes to the branch (`git push origin feature/amazing-feature`)
5. Open a pull request

## 📝 License

This open source project is licensed under the [MIT License] (LICENSE).
