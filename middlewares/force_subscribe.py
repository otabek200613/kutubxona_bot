from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler
from utils.check_sub import check_subscription_list
from data.config import CHANNELS


class ForceSubscribeMiddleware(BaseMiddleware):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    async def on_pre_process_message(self, message: types.Message, data: dict):
        user_id = message.from_user.id

        unsubscribed_channels = await check_subscription_list(self.bot, user_id, CHANNELS)

        if not unsubscribed_channels:
            return

        keyboard = types.InlineKeyboardMarkup(row_width=1)

        for channel_username in unsubscribed_channels:
            username_without_at = channel_username.replace('@', '')

            keyboard.add(types.InlineKeyboardButton(
                f"📢 Obuna bo‘lish ({channel_username})",
                url=f"https://t.me/{username_without_at}"
            ))

        keyboard.add(types.InlineKeyboardButton(
            "🔄 Obunani tekshirish",
            callback_data="check_sub"
        ))

        await message.answer(
            "🔒 Botdan foydalanish uchun talab qilingan **kanallarga** obuna bo‘ling!",
            reply_markup=keyboard,
            parse_mode="Markdown"
        )
        raise CancelHandler()

    async def on_pre_process_callback_query(self, call: types.CallbackQuery, data: dict):
        user_id = call.from_user.id

        unsubscribed_channels = await check_subscription_list(self.bot, user_id, CHANNELS)

        if unsubscribed_channels:
            await call.answer("❗ Barcha talab qilingan kanallarga obuna bo‘lmadingiz!", show_alert=True)
            raise CancelHandler()