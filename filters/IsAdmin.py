from aiogram.filters import BaseFilter
from aiogram.types import Message
from config_data.config import load_config_data

# admin_id = int(load_config_data().tgbot.admin)


class IsAdmin(BaseFilter):
    def __init__(self, admin_id: int) -> None:
        self.admin_id = admin_id

    async def __call__(self, msg: Message) -> bool:
        return msg.from_user.id == self.admin_id
