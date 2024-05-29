KPP_DB

Overview

KPP_DB is a Python-based project that features a Telegram bot designed to provide weather forecasts. Additionally, the project includes a script for encrypting and decrypting messages using the Russian alphabet. This README provides detailed instructions on how to set up and use both components of the project.

Features

Weather Bot
Retrieves real-time weather information for any city using the OpenWeatherMap API.
Supports English and Russian languages.
Interactive Telegram bot interface.
Encryption Script
Implements a two-stage encryption process using a Caesar cipher and transposition based on a keyword.
Allows secure encoding and decoding of messages in the Russian language.
Installation

Clone the repository:
sh
Копировать код
git clone https://github.com/KirillBurtsev/KPP_DB.git
Navigate to the project directory:
sh
Копировать код
cd KPP_DB
Install the required Python packages:
sh
Копировать код
pip install pyowm pyTelegramBotAPI
Weather Bot Setup

Configure Bot Token and API Key:

Create a configbot_wi.py file in the project directory.
Add your Telegram bot token and OpenWeatherMap API key in the following format:
python
Копировать код
token = 'YOUR_TELEGRAM_BOT_TOKEN'
key = 'YOUR_OPENWEATHERMAP_API_KEY'
Run the Bot:

Execute the bot script:
sh
Копировать код
python bot_script.py
Using the Bot:

Open Telegram and search for your bot.
Use /settings to change the language.
Send a city name to get the weather forecast.
Use /help to see available commands.
Encryption Script Usage

Run the Script:

Execute the encryption script:
sh
Копировать код
python encryption_script.py
Menu Options:

Encrypt a message: Press 1 and follow the prompts to input your message, shift key, and keyword.
Decrypt a message: Press 2 to decrypt the previously encrypted message using the same key and keyword.
Exit the program: Press 0.
Example
sh
Копировать код
Зашифровать сообщение, нажмите - "1"
Расшифровать сообщение, нажмите - "2"
Выйти из программы, нажмите - "0"
1
Введите строку: привет мир
Введите ключ: 3
Введите ключ-слово для 2-го этапа шифрования: ключ
Зашифрованное сообщение: тлйчзеопйс 

Расшифровать сообщение, нажмите - "2"
2
Расшифрованное сообщение: привет мир
Contributing

Fork the repository.
Create a new branch:
sh
Копировать код
git checkout -b feature-branch
Make your changes and commit them:
sh
Копировать код
git commit -m 'Add some feature'
Push to the branch:
sh
Копировать код
git push origin feature-branch
Open a pull request.
License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

For any questions or inquiries, please contact Kirill Burtsev.
