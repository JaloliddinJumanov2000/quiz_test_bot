from functools import wraps
from aiogram.types import Message
from utils.db.database import User, session
from keyboards.reply.button import menu
from aiogram.utils.i18n import gettext as _


def check_register(func):
    @wraps(func)
    async def wrapper(message: Message, *args, **kwargs):
        chat_id = message.from_user.id

        if User.check_register(session, chat_id):
            await message.answer(_("Siz allaqachon ro'yxatdan o'tgansiz!"), reply_markup=menu())
            return

        return await func(message, *args, **kwargs)

    return wrapper
