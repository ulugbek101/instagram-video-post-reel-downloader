from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def generate_main_menu():
    markup =  ReplyKeyboardMarkup(
        resize_keyboard=True,
        selective=True,
        one_time_keyboard=True)
    markup.add(
        "🔗 Havola yuborish",
    )
    return markup
