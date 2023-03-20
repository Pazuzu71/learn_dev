from aiogram import Router
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command, StateFilter, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state


from config_data.config import load_config_data
from lexicon.lexicon import LEXICON
from filters.IsAdmin import IsAdmin
from FSM.FSMGroups import Add
from keyboards.generation_kb import create_generation_kb


admin_id = int(load_config_data().tgbot.admin)


router = Router()
router.message.filter(
    IsAdmin(admin_id=admin_id)
)


# Этот хэндлен открывает меню хэлп для админа, в котором есть возможность пополнять базу мудрости
@router.message(Command(commands=['help']), StateFilter(default_state))
async def command_help(msg: Message):
    await msg.answer(text=LEXICON['/help_admin'])


# Этот хэндлер запускает машину состояний и просит выбрать тему мудрости
@router.message(Command(commands=['add']), StateFilter(default_state))
async def command_add(msg: Message, state: FSMContext):
    await msg.answer(text=LEXICON['theme'],
                     reply_markup=create_generation_kb(*LEXICON['themes'], LEXICON['cancel']))
    await state.set_state(Add.fill_theme)


# Этот хэндлер реагирует на нажатие кнопки "Отменить", происходит выход из машины состояний
@router.callback_query(~StateFilter(default_state), Text(text=LEXICON['cancel']))
async def process_cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer(text=LEXICON['/start'], reply_markup=create_generation_kb(LEXICON['generation']))


# Этот хэндлер проверяет, что выбрана тема из списка тем и просит написать мудрость
@router.callback_query(StateFilter(Add.fill_theme), Text(text=LEXICON['themes']))
async def theme_choice(callback: CallbackQuery, state: FSMContext):
    await state.update_data(gender=callback.data)
    await callback.message.delete()
    await callback.message.answer(text=LEXICON['info'])
    await state.set_state(Add.fill_text)


# Этот хэндлер дописывает мудрость в словать, словарь можно куда-то записать
@router.message(StateFilter(Add.fill_text))
async def get_info(msg: Message, state: FSMContext):
    print('111')
    await state.update_data(info=msg.text)
    dct = await state.get_data()
    print(dct)
    await state.clear()
