from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu_keybord = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=" ⌛️<b>Namoz vaqtlari</b>"),
         KeyboardButton(text="📖 <b>Quron</b>")],
    ],
    resize_keyboard=True
)