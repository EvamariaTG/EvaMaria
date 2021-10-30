import re
from os import environ
id_pattern = re.compile(r'^.\d+$')


# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/da19dda0d22cd8e414b3a.jpg https://telegra.ph/file/b44c0b631d24962f1763d.jpg https://telegra.ph/file/1182c47563d4d2056d333.jpg https://telegra.ph/file/7509e456f3c892059e58b.jpg https://telegra.ph/file/a0deb172cf6135ae01a17.jpg https://telegra.ph/file/62fcaafdb1260408f0217.jpg https://telegra.ph/file/a52bcaffb4fa3ceedff8b.jpg https://telegra.ph/file/9228d1701d399dfe31c4d.jpg https://telegra.ph/file/3fc87bd77b1c577f90ae8.jpg https://telegra.ph/file/bd4c0bce09d87bb3095da.jpg https://telegra.ph/file/997d7231f4a02d7d8de93.jpg https://telegra.ph/file/6db47a5a2b46e97b22228.jpg https://telegra.ph/file/58c885988c27b7dc41fe7.jpg https://telegra.ph/file/504bf54f95d594e05c061.jpg https://telegra.ph/file/561b10b96968e4dd51b9a.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', "").split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
