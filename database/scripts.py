import aiosqlite


async def create_tables():
    async with aiosqlite.connect('DB.sqlite') as conn:
        await conn.execute(
            '''CREATE TABLE IF NOT EXISTS wisdom(
            wisdom_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            wisdom TEXT,
            theme TEXT 
            )'''
                           )
        await conn.commit()
