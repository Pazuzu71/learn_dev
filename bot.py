import asyncio


from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


from config_data import config
from handlers import admin_handlers, user_handlers, other_handlers
from keyboards.main_menu import set_main_menu
from database.scripts import create_tables


TOKEN = config.load_config_data().tgbot.token


async def main():
    # создаем таблицы и базу, если еще нет
    await create_tables()
    # инициализируем хранилище
    storage: MemoryStorage = MemoryStorage()

    # создаем экземпляры бота и диспетчера
    bot: Bot = Bot(token=TOKEN, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=storage)

    # создаем главное меню
    await set_main_menu(bot)

    # подключаем роутеры
    dp.include_router(admin_handlers.router)
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # очищаем очередь апдейтов, запускаем поулинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Ошибка, остановка бота!')
