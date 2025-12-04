from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from middlewares.force_subscribe import ForceSubscribeMiddleware
from middlewares.throttling import ThrottlingMiddleware
from data.config import BOT_TOKEN
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
user_ids = set()

# Middleware ulash
dp.middleware.setup(ForceSubscribeMiddleware(bot))
dp.middleware.setup(ThrottlingMiddleware())
