from aiogram import Dispatcher

from loader import dp
from .private_chat import IsPrivate
from .is_admin import IsAdmin


if __name__ == "filters":
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsAdmin)
