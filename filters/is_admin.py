from aiogram.dispatcher.filters.filters import Filter
from aiogram.types import Message

from data.config import ADMINS


class IsAdmin(Filter):
    key = 'is_admin'

    async def check(self, message: Message) -> bool:
        return message.from_user.id in ADMINS
