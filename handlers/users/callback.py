# handlers/users/callback.py

from aiogram import types
from loader import dp, bot
# 1. CHANNELS ro'yxatini import qilamiz
from data.config import CHANNELS
# 2. To'g'ri funksiyani import qilamiz
from utils.check_sub import check_subscription_list


@dp.callback_query_handler(text="check_sub")  # yoki boshqa tegishli xandler
async def check_sub_handler(call: types.CallbackQuery):
    user_id = call.from_user.id

    # --- XATOSIZ QATOR ---
    # check_subscription_list funksiyasini barcha 3 ta argument bilan chaqiramiz
    unsubscribed_channels = await check_subscription_list(bot, user_id, CHANNELS)

    if unsubscribed_channels:
        # Hali obuna bo'lmagan kanallar bor
        await call.answer("❗ Siz hali barcha talab qilingan kanallarga obuna bo‘lmadingiz!", show_alert=True)
        # Middleware bu yerda tekshiradi, lekin agar xandler ichida bo'lsa, siz xabarni yangilashingiz mumkin

    else:
        # Barchasiga obuna bo'lgan
        await call.answer("✅ Siz barcha kanallarga obuna bo‘ldingiz!", show_alert=False)

        # Obuna tekshirilgandan so'ng foydalanuvchiga asosiy menyuni yuborish
        # (Bu yerda sizning start_button va boshqa logikangizni qo'shishingiz kerak)
        try:
            await call.message.delete()
        except Exception:
            pass

        # Asosiy xandlerga yuborish uchun start komandasini qayta ishga tushirish (yoki shu kabi funksiya)
        # Masalan: await call.message.answer("Xush kelibsiz!")