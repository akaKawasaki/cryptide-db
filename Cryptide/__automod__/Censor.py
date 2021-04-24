# -*- coding: utf-8 -*-

"""
Cryptide Censoring Cog
~~~~~~~~~~~~~~~~~~~~~~

This is where the censor functionality resides.

:copyright: (c) 2021 Trenton "Kawasaki" G
:terms: No Public Use
:visibilty: Private Cog

"""

from discord.ext import commands

class Censor(commands.Cog, name="Censor"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        #advert detector
        if "discord.gg" in message.content.lower():
            await message.delete()
            await message.channel.send("Don't advertise your server")

        #nword detector
        if "nigger" in message.content.lower():
            await message.delete()
            await message.channel.send(f"Imagine being a racist {message.author.mention}.")
        elif "nogger" in message.content.lower():
            await message.delete()
            await message.channel.send(f"Imagine bypassing {message.author.mention}")
        elif "nigga" in message.content.lower():
            await message.delete()
            await message.channel.send(f"Sorry {message.author.mention}. It's against TOS :(")
        elif "niga" in message.content.lower():
            await message.delete()
            await message.channel.send(f"Imagine bypassing {message.author.mention}")
        elif "niger" in message.content.lower():
            await message.delete()
            await message.channel.send(f"Imagine bypassing {message.author.mention}")
      
def setup(bot):
    bot.add_cog(Censor(bot))