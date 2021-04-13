# -*- coding: utf-8 -*-

"""
Cryptide EasterEgg Cog
~~~~~~~~~~~~~~~~~~~~~~

Seceret Unknown Commands Belong Here

:copyright: (c) 2021 Trenton "Kawasaki" G
:terms: No Public Use
:visibilty: Private Cog

"""

#Discord
import discord
from discord.ext import commands

#Other
import random

class EasterEggs(commands.Cog, name="EasterEggs"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="amogus", aliases=["sus", "sussy"])
	async def amogus(self, ctx):
		embed = discord.Embed(description=f"**{chr(3497)}**", color=0x7289DA)
		await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(EasterEggs(bot))