from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router, Bot
from lexicon.lexicon import LEXICON
from keyboards.generation_kb import create_generation_kb


router = Router()


@router.message(CommandStart())
async def command_start(msg: Message):
    await msg.answer(text=LEXICON['/start'], reply_markup=create_generation_kb(LEXICON['generation']))


@router.message(Command(commands=['help']))
async def command_help(msg: Message):
    await msg.answer(text=LEXICON['/help'])


