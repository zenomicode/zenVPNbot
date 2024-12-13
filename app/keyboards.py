from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder





menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Мои ключи", callback_data="menu_keys"), InlineKeyboardButton(text="Помощь", callback_data="menu_help")],
    [InlineKeyboardButton(text="Все о RKN VPN", callback_data="menu_about"), InlineKeyboardButton(text="Пожертвовать", callback_data="menu_donat")]
])