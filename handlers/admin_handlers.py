from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from config_data.config import load_config_data
from lexicon.lexicon import LEXICON
from filters.IsAdmin import IsAdmin


admin_id = int(load_config_data().tgbot.admin)


router = Router()
router.message.filter(
    IsAdmin(admin_id=admin_id)
)


@router.message(Command(commands=['help']))
async def command_help(msg: Message):
    await msg.answer(text=LEXICON['/help_admin'])


@router.message(Command(commands=['add']))
async def command_add(msg: Message):
    await msg.answer(text=LEXICON['add_admin'])

