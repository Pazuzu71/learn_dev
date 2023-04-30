from datetime import datetime as dt
from random import randint


from aiogram.filters import CommandStart, Command, StateFilter, Text
from aiogram.types import Message, CallbackQuery
from aiogram import Router
from aiogram.fsm.state import default_state


from lexicon.lexicon import LEXICON
from keyboards.generation_kb import create_generation_kb
from database.scripts import get_user, insert_user, get_wisdom, get_wisdom_max_id


router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def command_start(msg: Message):
    if not await get_user(msg.from_user.id):
        await insert_user(msg.from_user.id, dt.now())
    await msg.answer(text=LEXICON['/start'], reply_markup=create_generation_kb(LEXICON['generation']))


@router.message(Command(commands=['help']), StateFilter(default_state))
async def command_help(msg: Message):
    await msg.answer(text=LEXICON['/help'])


@router.callback_query(StateFilter(default_state), Text(text=LEXICON['generation']))
async def wisdom_gen(callback: CallbackQuery):
    print('дошло до генерации')
    wisdom_max_id = await get_wisdom_max_id()
    print(wisdom_max_id[0])
    wisdom_id = randint(1, wisdom_max_id[0])
    print('wisdom_id', wisdom_id)
    answer = await get_wisdom(wisdom_id)
    print(type(answer))
    await callback.message.answer(text=answer[0])
