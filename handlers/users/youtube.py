from aiogram import types
from api import youtube
from loader import dp



@dp.message_handler()
async def process_youtube_link(msg: types.Message):
    link = await youtube(msg.text)
    await msg.answer(link)



