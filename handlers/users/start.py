from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types  import Message
from loader import dp
from keyboards.default import menu_keybord
@dp.message_handler(CommandStart())
async def bot_start(message: Message):
   info = f"Assalomu aleykum, {message.from_user.full_name}\n"
   info+= f"AL-QURAN  botiga xush kelibsiz!"
   await message.answer(info,reply_markup=menu_keybord)

