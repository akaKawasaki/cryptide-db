# -*- coding: utf-8 -*-

"""
Cryptide Misc Cog
~~~~~~~~~~~~~~~~~

This Allows Misc Commands That Need/Use Cog Functions To Be Used As An Extension.
This Is The Main Cog For Listeners.

:copyright: (c) 2021 Trenton "Kawasaki" G
:terms: No Public Use
:visibilty: Private Cog

"""

#Discord
import discord
from discord.ext import commands

#Others
import humanize
import datetime
import time
import sys
import asyncio
#import COVID19Py as covidStats
from authgen import Generator
import json
import nekos
import os
import random
from PIL import Image

class Misc(commands.Cog, name="Misc"):
	def __init__(self, bot):
		#Defining The Bot Variable
		self.bot = bot

		#Uptime And What-not
		self.start_time = datetime.datetime.now()

		#Bot Info
		self.title = "Bot"
		self.version = "2.4.6 Full Release"

		#Pass Generator
		self.generator = Generator

		#Snipe
		self.last_msg = None

		#Covid
		#self.covid19 = covidStats.COVID19(data_source="csbs")
		#self.latest = self.covid19.getLatest()
		#self.confirms = self.covid19.getLatest()["confirmed"]
		#self.deaths = self.covid19.getLatest()["deaths"]

	@commands.Cog.listener()
	async def on_message_delete(self, message: discord.Message):
		self.last_msg = message

	@commands.command(name="snipe")
	async def snipe(self, ctx: commands.Context):
		if not self.last_msg:
			await ctx.send("There is no message to snipe!")
			return

		author = self.last_msg.author
		content = self.last_msg.content
		channel = self.last_msg.channel.id

		embed = discord.Embed(title=f"Sniped A Message :p", color=0xC0C0C0)
		embed.set_thumbnail(url=author.avatar_url)
		embed.add_field(name="**Author:**", value=author.mention, inline=False)
		embed.add_field(name="**Message:**", value=f"`{content}`", inline=False)
		embed.add_field(name="**Channel**", value=f"<#{channel}>", inline=False)
		await ctx.send(embed=embed)

	@commands.command(name="randcolor")
	async def rcol(self, ctx):
	    r = random.randrange(0, 255)
	    g = random.randrange(0, 255)
	    b = random.randrange(0, 255)
	    Image.new('RGB', (96, 96), (r, g, b)).save("RANDOMCOLOR.png")
	    await ctx.send(f"R{r}, G{g}, B{b}", file=discord.File("RANDOMCOLOR.png"))
	    os.system("del RANDOMCOLOR.png")

	"""
	@commands.command(name="covid")
	async def covid(self, ctx):
		embed = discord.Embed(title=f"Covid Stats", color=0xC0C0C0)
		embed.add_field(name="__Confirmed Cases__", value=f"`{self.confirms}`", inline=False)
		embed.add_field(name="__Deaths__", value=f"`{self.deaths}`", inline=False)

		await ctx.send(embed=embed)
	"""

	@commands.command(name="botinfo")
	async def botstats(self, ctx):
		serverCount = len(self.bot.guilds)
		memberCount = len(set(self.bot.get_all_members()))

		await ctx.send(f"{self.title} v{self.version}, discord.py `{discord.__version__}`, `Python {sys.version}` on `{sys.platform}`.\n\nServer Count: `{serverCount}`\nMember Count: `{memberCount}`\n{self.title} was loaded `{humanize.naturaltime(self.start_time)}`.")

	@commands.command(name="uptime")
	async def upmyboy(self, ctx):
	    await ctx.send(f"My current instance was started `{humanize.naturaltime(self.start_time)}`.")

	@commands.command()
	async def vote(self, ctx):
	    embed = discord.Embed(title=f'Upvote Me!', description='Here is the link to upvote me. Click it!', colour=0xC0C0C0, timestamp=ctx.message.created_at)

	    embed.add_field(name='**Top.gg**', value="https://top.gg/bot/811349622709944390/vote", inline=False)
	    embed.add_field(name='**DBL**', value="https://discordbotlist.com/bots/cryptide/upvote", inline=False)
	    embed.add_field(name='**Discord Boats**', value="https://discord.boats/bot/811349622709944390/vote", inline=False)

	    embed.set_footer(text=f"Carpe Noctem | {self.bot.user.name}")
	    embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

	    await ctx.send(embed=embed)

	@commands.command(name="passgen")
	async def password_generator(self, ctx):
	    password = self.generator.random_medium(length=24)
	    await ctx.author.send(f"Password: **{password}**")
	    await ctx.send(f"Hey {ctx.author.mention}, I DM'ed you your generated password!")

	@commands.command()
	async def invite(self, ctx):
	    embed = discord.Embed(description='[Click Me :D](https://discord.com/api/oauth2/authorize?client_id=811349622709944390&permissions=8&scope=bot)', colour=0xC0C0C0, timestamp=ctx.message.created_at)

	    embed.set_footer(text=f"Carpe Noctem | {self.bot.user.name}")
	    embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

	    await ctx.send(embed=embed)

	@commands.command()
	async def ping(self, ctx):
		start = time.time()
		message = await ctx.send("Pinging...")
		end = time.time()
		await message.edit(content=f'**Bot latency**: {round (self.bot.latency * 1000)}ms\n**Websocket latency**: {round((end - start) * 1000)}ms')

	@commands.command()
	async def whois(self, ctx, member: discord.Member = None):
	    member = ctx.author if not member else member
	    roles = [role for role in member.roles]

	    embed=discord.Embed(colour=0xC0C0C0, timestamp=ctx.message.created_at)
	    
	    embed.set_author(name=f"Who Is {member}")
	    embed.set_thumbnail(url=member.avatar_url)
	    embed.set_footer(text=f"Carpe Noctem | {self.bot.user.name}")
	    
	    embed.add_field(name="ID:", value=member.id, inline=False)
	    embed.add_field(name="Display name:", value=member.display_name, inline=False)

	    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC"), inline=False)
	    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC"), inline=False)
	    
	    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False)
	    embed.add_field(name="Top role:", value=member.top_role.mention, inline=False)
	    
	    embed.add_field(name="Bot?", value=member.bot, inline=False)

	    await ctx.send(embed=embed)

	@commands.command()
	async def nsfwcheck(self, ctx):
	    if ctx.channel.is_nsfw():
	       await ctx.send("This is a valid NSFW channel.")
	    else:
	        await ctx.send("This is not a NSFW channel.")

	@commands.command()
	@commands.cooldown(1, 90, commands.BucketType.user)
	async def echo(self, ctx, *, message=None):
		message = message or "Please provide the message to be repeated."
		await ctx.message.delete()
		await ctx.send(message)

	@echo.error
	async def echo_error(self, ctx, error):
	    if isinstance(error, commands.CommandOnCooldown):
	        await ctx.send("Hey did you forget something?")

def setup(bot):
    bot.add_cog(Misc(bot))