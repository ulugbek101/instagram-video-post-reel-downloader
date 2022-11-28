from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from filters.private_chat import IsPrivate
from keyboards.default.main_menu import generate_main_menu


@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message):
    try:
        db.register_user(telegram_id=message.from_user.id,
                         fullname=message.from_user.full_name,
                         username=message.from_user.username)
    except:
        pass
    await message.answer(
        text=f"<i>Assalomu alaykum, <b>{message.from_user.full_name}</b></i> 👋\n\n"
             f"<i>Bot <b>ALFA-TEST</b> rejimida ishlamoqda, kamchilik va \"BUG\" lar kuzatilganida, </i>"
             f"<i>iltimos @Umaraliyev_U ga xabar bering</i>",
        reply_markup=generate_main_menu()
    )
