from environs import Env
env = Env()
env.read_env()
ADMINS = env.list("ADMINS")
IP = env.str("ip")
CHANNELS = env.list("CHANNELS")
BOT_TOKEN = env.str("BOT_TOKEN")