from datetime import datetime as dt


from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.state import default_state


from lexicon.lexicon import LEXICON
from keyboards.generation_kb import create_generation_kb
from database.scripts import get_user, insert_user


router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def command_start(msg: Message):
    if not await get_user(msg.from_user.id):
        await insert_user(msg.from_user.id, dt.now())
    await msg.answer(text=LEXICON['/start'], reply_markup=create_generation_kb(LEXICON['generation']))


@router.message(Command(commands=['help']), StateFilter(default_state))
async def command_help(msg: Message):
    await msg.answer(text=LEXICON['/help'])
