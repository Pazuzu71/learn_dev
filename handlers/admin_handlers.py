from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state


from config_data.config import load_config_data
from lexicon.lexicon import LEXICON
from filters.IsAdmin import IsAdmin
from FSM.FSMGroups import Add


admin_id = int(load_config_data().tgbot.admin)


router = Router()
router.message.filter(
    IsAdmin(admin_id=admin_id)
)


# Этот хэндлен открывает меню хэлп для админа, в котором есть возможность пополнять базу мудрости
@router.message(Command(commands=['help']), StateFilter(default_state))
async def command_help(msg: Message):
    await msg.answer(text=LEXICON['/help_admin'])


# Этот хэндлер просит занести новую мудрость в окне ввода текста
@router.message(Command(commands=['add']), StateFilter(default_state))
async def command_add(msg: Message):
    await msg.answer(text=LEXICON['add_admin'])

