from discord.ext import commands

class DiscordBot(commands.Bot):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, command_prefix, discord_token, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.token = discord_token

    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')
