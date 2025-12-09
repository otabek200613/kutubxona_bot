import os
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()  # Agar .env boshqa joyda bo'lsa, path berish mumkin: load_dotenv("/home/otabek/Рабочий стол/kutubxona_bot-main/.env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN .env faylida topilmadi!")

# ADMINS ro'yxati
ADMIN_ID = os.getenv("ADMINS")
if ADMIN_ID is not None:
    ADMIN_ID = int(ADMIN_ID)
ADMINS = [ADMIN_ID] if ADMIN_ID else []
