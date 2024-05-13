from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"✅ Assalomu Alaykum, {message.from_user.full_name}! \n✅ Ushbu Bot You Tube videoni MP3 formatda yuklab beradi \n✅ Botdan foydalanish uchun You Tube link yuboring")
