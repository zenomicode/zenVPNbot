from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import app.keyboards as kb
# from middlewares import BaseMiddleware

user = Router()

# user.message.middleware(BaseMiddleware())
@user.callback_query(F.data("back"))
@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"""
Привет, {message.from_user.full_name} 👋

RKN VPN - быстрый и безопасный доступ к свободному интернету без ограничений

🌐 Доступ к любым социальным сетям
💻 Анонимность
🤫 Устойчивость к блокировкам
🚀 Высокая скорость
🤳 Поддержка любых устройств
🙅 Нет рекламы

⇩ Главное меню  ⇩
                         """, reply_markup=kb.menu)



@user.callback_query(F.data("menu_keys"))
async def list_keys(callback: CallbackQuery):
    await callback.answer("Функционал не доступен")
    
    
    
@user.callback_query(F.data("menu_about"))
async def about(callback: CallbackQuery):
    await callback.answer("Функционал не доступен")
    
    
    
@user.callback_query(F.data("menu_donat"))
async def donat(callback: CallbackQuery):
    await callback.answer("Функционал не доступен")
    
    
    
@user.callback_query(F.data("menu_help"))
async def cmd_help(callback: CallbackQuery):
    await callback.answer("Функционал не доступен")
    
    
    