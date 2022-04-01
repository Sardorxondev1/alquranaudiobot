from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types  import Message
from loader import dp
from keyboards.default import menu_keybord
@dp.message_handler(CommandStart())
async def bot_start(message: Message):
   info = f"<b>Assalomu aleykum, {message.from_user.full_name}\n</b>"
   info+= f"<b>AL-QURAN  botiga xush kelibsiz! </b>"
   await message.answer(info,reply_markup=menu_keybord)

