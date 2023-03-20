from aiogram.filters.state import State, StatesGroup


class Add(StatesGroup):
    fill_theme = State()
    fill_text = State()
