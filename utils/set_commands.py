from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Botni ishga tushirish'),
        BotCommand(command='help', description='Botni ishga tushirish'),

    ]
    await bot.set_my_commands(commands=commands)