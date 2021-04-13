from discord.ext import commands
from AntiSpam import AntiSpamHandler
from AntiSpam.ext import AntiSpamTracker
import json

class Antispam(commands.Cog, name="Antispam"):
    def __init__(self, bot):
        self.bot = bot
        self.bot.handler = AntiSpamHandler(self.bot)

        self.bot.handler.add_ignored_item(370120271367110656, "member") #NullPointer
        self.bot.handler.add_ignored_item(786334287968337981, "member") #Me
        self.bot.handler.add_ignored_item(382687991958601729, "member") #Prime Iridium
        self.bot.handler.add_ignored_item(705641763062415431, "member") #Micah
        self.bot.handler.add_ignored_item(490690957642301442, "member") #Matthew Tibbits
        self.bot.handler.add_ignored_item(264445053596991498, "guild") #Top.gg

    @commands.Cog.listener()
    async def on_message(self, message):
        await self.bot.handler.propagate(message)
      
def setup(bot):
    bot.add_cog(Antispam(bot))