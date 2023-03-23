import aiosqlite

#TODO параметризировать путь до базы
async def create_tables():
    async with aiosqlite.connect('DB.sqlite') as conn:
        await conn.execute(
            '''CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            user_tg_id INTEGER,
            last_activity TEXT,
            create_date TEXT
            )'''
        )
        await conn.execute(
            '''CREATE TABLE IF NOT EXISTS wisdom(
            wisdom_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            theme TEXT,
            wisdom TEXT,
            user_id INTEGER,
            create_date TEXT,
            FOREIGN KEY (user_id)  REFERENCES users (user_id)
            )'''
                           )
        await conn.commit()

#TODO убрать аргс, заносить конкретные параметры
# TODO в вставку добавить ид пользователя автора мудрости
async def insert_wisdom(*args):
    async with aiosqlite.connect('DB.sqlite') as conn:
        try:
            await conn.execute(
                '''INSERT INTO wisdom(theme, wisdom, create_date) VALUES (?,?,?)''', args
            )
            await conn.commit()
        except Exception as e:
            print('insert_wisdom', e)


async def insert_user(user_tg_id: int, *args):
    print(user_tg_id, type(user_tg_id), args)
    async with aiosqlite.connect('DB.sqlite') as conn:
        try:
            await conn.execute(
                '''INSERT INTO users(user_tg_id, create_date) VALUES (?, ?)''', (user_tg_id, *args)
            )
            await conn.commit()
        except Exception as e:
            print('insert_user', e)


async def get_user(tg_user_id: int):
    async with aiosqlite.connect('DB.sqlite') as conn:
        user = await conn.execute(
            '''SELECT user_id FROM users WHERE user_tg_id = ?''', (tg_user_id,)
        )
        return await user.fetchone()

