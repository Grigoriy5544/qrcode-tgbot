from aiogram import Bot, types, Dispatcher, executor
import qrcode
import os

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет")

@dp.message_handler()
async def process_help_command(message: types.Message):
    text = message.text
    img = qrcode.make(text)
    img.save('qrcode.png')
    photo = open('qrcode.png', 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    os.remove('qrcode.png')


if __name__ == '__main__':
    executor.start_polling(dp)