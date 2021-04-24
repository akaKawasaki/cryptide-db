# -*- coding: utf-8 -*-

"""
Cryptide Listener Cog
~~~~~~~~~~~~~~~~~~~~~

The listener Functionality Resides Here.

:copyright: (c) 2021 Trenton "Kawasaki" G
:terms: No Public Use
:visibilty: Private Cog

"""

import discord
from discord.ext import commands

class Listeners(commands.Cog, name="Listeners"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-----\nLogged in as: {self.bot.user.name} : {self.bot.user.id}\n-----\nMy current prefix is: c!\n-----")
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(self.bot.users)} Users | c!help"))

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        #Ignore these errors
        ignored = (commands.CommandNotFound, commands.UserInputError)

        if isinstance(error, ignored):
            return

        #Begin error handling
        if isinstance(error, commands.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)
            if int(h) == 0 and int(m) == 0:
                await ctx.send(f' You must wait {int(s)} seconds to use this command!')
            elif int(h) == 0 and int(m) != 0:
                await ctx.send(f' You must wait {int(m)} minutes and {int(s)} seconds to use this command!')
            elif int(h) == 0 and int(m) == 0 and int(s) !=0:
                await ctx.send(f' You must wait {int(h)} hours, {int(m)} minutes and {int(s)} seconds to use this command!')
            else:
                print(error)
        raise error

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await guild.owner.send(f"Hi! I'm Cryptide. Thanks For Welcoming Me To `{guild.name}`! My Command Prefix Is `c!` or `--`. I'm A Multipurpose Utiliy Bot! If you'd like a more informative lecture, use the command `c!help")
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(self.bot.users)} Users | c!help"))

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(self.bot.users)} Users | c!help"))

      
def setup(bot):
    bot.add_cog(Listeners(bot))