from aiogram.types import MediaGroup, InputFile
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from loader import dp
from forms import GetLink
from utils.get_content import get_content


@dp.message_handler(Text(equals="🔗 Havola yuborish", ignore_case=True))
async def request_link(message: Message):
    await message.delete()
    await GetLink.link.set()
    await message.answer(
        text="<i>🔗 Havolani shu yerga qo'ying </i>👇"
    )


@dp.message_handler(state=GetLink.link)
async def get_link(message: Message, state: FSMContext):
    await message.delete()
    msg = await message.answer(
        text="<i>Biroz kuting ...</i>"
    )
    file = get_content(
        unknown_link=message.text,
        telegram_id=message.from_user.id
    )

    if file:
        if file['many']:
            # Creating media group to group files
            media = MediaGroup()

            # Opening every file
            for i, path in enumerate(file['file_name']):
                media.attach_photo(photo=InputFile(path),
                                   caption='😎✅')

            await message.answer_media_group(
                media=media
            )


        else:
            with open(file=file['file_name'], mode='rb') as f:
                if file['extension'] == 'mp4':
                    await message.answer_video(
                        video=f,
                        caption='😎✅'
                    )
                else:
                    await message.answer_photo(
                        photo=f,
                        caption='😎✅'
                    )
    else:
        await message.answer(
            text="<i>📽️ Story / 🎇 Post / 🎞️ Reel ni olishda muammo yuzaga keldi, bu muammo siz yuborgan foydalanuvchi profili yopiq bo'lishidan kelib chiqgan bo'lishi mumkin </i>"
        )
        print(file)
    await dp.bot.delete_message(
        chat_id=message.chat.id,
        message_id=msg.message_id
    )
    await state.finish()

