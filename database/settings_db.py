import motor.motor_asyncio
from info import DATABASE_NAME, DATABASE_URI


class Settings:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.sett = self.db.settings

    def new_settings(self, chat_id, lock):
        return dict(
            chat_id=str(chat_id),
            button=lock, botpm=lock,
            file_secure=lock, imdb=lock,
            spell_check=lock, welcome=lock,
        )

    async def add_settings(self, chat_id, locked):
        locks = self.new_settings(chat_id, locked)
        await self.sett.insert_one(locks)

    async def is_settings_exist(self, chat_id):
        locks = await self.sett.find_one({'chat_id': int(chat_id)})
        return bool(locks)

    async def get_settings(self, chat_id):
        query = await self.sett.find_one({'chat_id': int(chat_id)})
        if query is not None:
            return query
        else:
            return None

    async def update_settings(self, chat_id, sett_type, lock):
        if sett_type == "button":
            await self.sett.update_one({'chat_id': chat_id}, {'$set': {'button': lock}})
        elif sett_type == "botpm":
            await self.sett.update_one({'chat_id': chat_id}, {'$set': {'botpm': lock}})
        elif sett_type == "file_secure":
            await self.sett.update_one({'chat_id': chat_id}, {'$set': {'file_secure': lock}})
        elif sett_type == "imdb":
            await self.sett.update_one({'chat_id': chat_id}, {'$set': {'imdb': lock}})
        elif sett_type == "spell_check":
            await self.sett.update_one({'chat_id': chat_id}, {'$set': {'spell_check': lock}})
        elif sett_type == "welcome":
            await self.sett.update_one({'chat_id': chat_id}, {'$set': {'welcome': lock}})


sett_db = Settings(DATABASE_URI, DATABASE_NAME)
