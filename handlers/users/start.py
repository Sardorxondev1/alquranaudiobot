from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types  import Message
from loader import dp
from keyboards.default import menu_keybord
@dp.message_handler(CommandStart())
async def bot_start(message: Message):
   await message.answer(f"Salom ",reply_markup=menu_keybord)

