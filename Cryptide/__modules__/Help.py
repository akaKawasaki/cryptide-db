# -*- coding: utf-8 -*-

"""
Cryptide Help Cog
~~~~~~~~~~~~~~~~~

Cog Version Of The Help Commands

:copyright: (c) 2021 Trenton "Kawasaki" G
:terms: No Public Use
:visibilty: Private Cog

"""

#Discord
import discord
from discord.ext import commands

#Other
import time
import asyncio

class Help(commands.Cog, name="Help"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="commands", aliases=["cmds", "cmdlist"])
	async def embede(self, ctx):
	    imageUrl = self.bot.user.avatar_url
	    embed = discord.Embed(title=f'Modules', description='Here are all of my Modules!', colour=0xC0C0C0, timestamp=ctx.message.created_at)

	    embed.add_field(name='• **__Mod Commands__**', value="`c!mod`", inline=True)
	    embed.add_field(name='• **__Info Commands__**', value="`c!info`", inline=True)
	    embed.add_field(name='• **__Misc Commands__**', value="`c!misc`", inline=True)
	    embed.add_field(name='• **__Owner Commands__**', value="`c!owner`", inline=True)
	    embed.add_field(name='• **__NSFW Commands__**', value="`c!nsfw`", inline=True)
	    embed.add_field(name='• **__Fun Commands__**', value="`c!fun`", inline=True)
	    embed.add_field(name='• **__Social Commands__**', value="`c!social`", inline=True)
	    embed.set_thumbnail(url=imageUrl)
	    embed.set_footer(text=f"Carpe Noctem | {self.bot.user.name}")
	    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

	    await ctx.send(embed=embed)

	@commands.command("mod")
	async def embed4(self, ctx):

	    embed = discord.Embed(title=f'Moderation Commands', description='Here are my mod Modules!', colour=0xC0C0C0, timestamp=ctx.message.created_at)

	    embed.add_field(name='Deletes messages with ease', value="`c!purge <message_amount>`", inline=False)
	    embed.add_field(name='Kicks somebody from the Server', value="`c!kick <@user_of_choice> <reason>`", inline=False)
	    embed.add_field(name='Bans somebody from the Server', value="`c!ban <@user_of_choice> <reason>`", inline=False)
	    embed.add_field(name='Unbans somebody from the Server', value="`c!unban <@user_thats_banned>`", inline=False)

	    embed.set_footer(text=f"Carpe Noctem | {self.bot.user.name}")
	    embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

	    await ctx.send(embed=embed)

	@commands.command("info")
	async def embed3(self, ctx):

	    embed = discord.Embed(title=f'Info Commands', description='Here are my info Modules!', colour=0xC0C0C0, timestamp=ctx.message.created_at)

	    embed.add_field(name='Shows the bots latency', value="`c!ping`", inline=False)
	    embed.add_field(name='Checks for NSFW Channels', value="`c!nsfwcheck`", inline=False)
	    embed.add_field(name='Shows info on a specific user', value="`c!whois <@user>`", inline=False)
	    embed.add_field(name='Bot uptime', value="`c!uptime`", inline=False)
	    embed.add_field(name='Shows statistics of the bot', value="`c!botinfo`", inline=False)
	    embed.add_field(name='Gives you a documentation link for an entity.', value="`c!rtfm <api_ref_example>`", inline=False)

	    embed.set_footer(text=f"Carpe Noctem | {self.bot.user.name}")

	    await ctx.send(embed=embed)

	@commands.command("misc")
	async def embed2(self, ctx):

	    embed = discord.Embed(title=f'Misc Commands', description='Here are my misc Modules!', colour=0xC0C0C0, timestamp=ctx.message.created_at)

	    embed.add_field(name='Shows the bots invite link', value="`c!invite`", inline=False)
	    embed.add_field(name='Generates A Random Password', value="`c!passgen`", inline=False)
	    embed.add_field(name='Shows the vote link', value="`c!vote`", inline=False)
	    #easter egg embed.add_field(name='Sus', value='`c!amogus`', inline=False)
	    #embed.add_field(name="Gets current covid stats in the whole world", value='`c!covid`', inline=False)
	    embed.add_field(name='Snipes a deleted message', value="`c!snipe`", inline=False)
	    embed.add_field(name='Generate a random RGB Color', value="`c!randcolor`", inline=False)

	    embed.set_footer(text=f"Carpe Noctem | {self.bot.user.name}")
	    embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

	    await ctx.send(embed=embed)

#The NAFW Help Has Been Moved To The NSFW.py cog.

	@commands.command("fun")
	async def embedoi(self, ctx):

	    embed = discord.Embed(title=f"Fun", description='Fun Commands!', colour=0xC0C0C0, timestamp=ctx.message.created_at)

	    embed.add_field(name='Roles a 6 sided dice', value="`c!dice`", inline=False)
	    embed.add_field(name='Bot answers a question', value="`c!8ball <question>`", inline=False)
	    embed.add_field(name='Sends an embed message out to the chat. (it doesnt ping btw)', value="`c!poll <message>`", inline=False)
	    embed.add_field(name='Flips a coin.', value="`c!flip`", inline=False)
	    #embed.add_field(name='Tells A Rape Joke.', value="`c!rjoke`", inline=False)
	    embed.add_field(name='Tells A Dad Joke.', value="`c!djoke`", inline=False)

	    embed.set_footer(text=f"Carpe Noctem | {self.bot.user.name}")
	    embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

	    await ctx.send(embed=embed)

	@commands.command("social")
	async def embedi(self, ctx):

	    embed = discord.Embed(title=f"Social", description='Social Commands!', colour=0xC0C0C0, timestamp=ctx.message.created_at)

	    embed.add_field(name='Makes the bot say anything', value="`c!echo <any_message_you_want>`", inline=False)
	    embed.add_field(name='Slaps somebody', value="`c!slap <@user>`", inline=False)
	    embed.add_field(name='Kiss somebody', value="`c!kiss <@user>`", inline=False)
	    embed.add_field(name='Hug somebody', value="`c!hug <@user>`", inline=False)
	    embed.add_field(name='Feed somebody', value="`c!feed <@user>`", inline=False)
	    embed.add_field(name='Tickle somebody', value="`c!tickle <@user>`", inline=False)
	    embed.add_field(name='Poke somebody', value="`c!poke <@user>`", inline=False)
	    embed.add_field(name='Insult somebody', value="`c!bully <@user>`", inline=False)

	    embed.set_footer(text=f"Carpe Noctem | {self.bot.user.name}")
	    embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

	    await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Help(bot))
