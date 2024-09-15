from aiogram import Bot, Dispatcher, types 
from aiogram.filters.command import Command
import asyncio
import logging 
with open('C:/Users/07880/YandexDisk/програмирование/telegrambot/token.txt', 'r', encoding='utf-8') as f:
    token_bot = f.read(46)

logging.basicConfig(level=logging.INFO)
bot_token = Bot(token=token_bot)
dp = Dispatcher()

@dp.message(Command("start"))
async def async_start(message:types.Message):
    await message.answer("Прекрасный день, не правда ли?")

async def main():
    await dp.start_polling(bot_token)

if __name__ == "__main__" :
    asyncio.run(main())

