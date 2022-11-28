from aiogram.dispatcher.filters import Filter
from aiogram.types import Message


class IsPrivate(Filter):
    key = 'is_private'

    async def check(self, message: Message) -> bool:
        return message.chat.type == 'private'
