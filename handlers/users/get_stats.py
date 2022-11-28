from aiogram.types import Message

from loader import dp, db
from filters.is_admin import IsAdmin


@dp.message_handler(IsAdmin(), commands='stats')
async def get_stats(message: Message):
    users = db.get_users()

    msg = "<i>--- Barcha Foydalanuvchilar ---</i>\n\n"
    msg += f"<i>Foydalanuvchilar soni: <b>{len(users)} ta</b></i>\n\n"
    for user in users:
        msg += f"{user[0]} {'-'*20}\n"
        msg += f"Ism: <i>{user[-2]}</i>\n"
        msg += f"Username: @{user[-1]}\n\n"

    await message.answer(
        text=msg
    )



