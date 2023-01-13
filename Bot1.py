from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
import sqlite3
b1 = KeyboardButton('Кнопка')
kb = ReplyKeyboardMarkup()
gk = ReplyKeyboardRemove()
kb.row(b1, b1)
k = 5.5
bot = Bot(token='5920353752:AAGvOaEVPaEem-W95dWv77bu7OjxeoNhF8U')
dp = Dispatcher(bot)
ur= InlineKeyboardMarkup(0)
urlbk = InlineKeyboardMarkup(row_width=7)
urbut = InlineKeyboardButton(text='*', callback_data='/f')
urlbk.add(urbut)
@dp.message_handler(commands=['f5'])
async def echo_send(message : types.Message):
    # await message.reply(message.text)
    await bot.send_message(message.from_user.id, message.from_user.id, reply_markup = kb)
@dp.callback_query_handler(text='ddd')
async def echo_send(callback : types.callback_query):
    # await message.reply(message.text)
    await bot.send_message('kjikj')
@dp.message_handler()
async def echo_send(message : types.Message):
    # await message.reply(message.text)
    await bot.send_message(message.from_user.id, message.from_user.id, reply_markup = gk)
executor.start_polling(dp, skip_updates=True)