from dataclasses import dataclass


from environs import Env


@dataclass
class TgBot:
    token: str
    admin: int


@dataclass
class DB:
    path: str


@dataclass
class Config:
    tgbot: TgBot
    database: DB


def load_config_data(path: str | None = None):
    env = Env()
    env.read_env(path=path)
    return Config(
        tgbot=TgBot(
            token=env('TOKEN'),
            admin=env('ADMIN_ID')
        ),
        database=DB(
            path=env('PATH')

        )
    )
