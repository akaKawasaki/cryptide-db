# -*- coding: utf-8 -*-

"""
Cryptide Forbidden Cog
~~~~~~~~~~~~~~~~~~~~~~

This Allows Forbidden/Owner/Test Commands That Need/Use Cog Functions To Be Used As An Extension.

:copyright: (c) 2021 Trenton "Kawasaki" G
:terms: No Public Use
:visibilty: Private Cog

"""

#Discord
import discord
from discord.ext import commands

#Others
from akaneko import akaneko
import random
import ast
from AntiSpam.Util import transform_message
from discord.ext.buttons import Paginator
from __utils__.util import *

class Forbidden(commands.Cog, name="Forbidden"):
	def __init__(self, bot):
		self.bot = bot

	#This command exists for security reasons. don't remove my bot ;-;
	@commands.command()
	async def servers(self, ctx):
	    activeservers = self.bot.guilds
	    for guild in activeservers:
	        await ctx.send(f"`{guild.name}` : `{guild.id}`")

	@commands.command(aliases=['disconnect', 'close', 'stopbot'])
	@commands.is_owner()
	async def logout(self, ctx):
	    await ctx.send(f"Hasta Luego :wave:")
	    await self.bot.close()

	@commands.command("test")
	@commands.is_owner()
	async def testing(self, ctx):
	    await ctx.send(f"I work as intended :D")

	@commands.command(name="owner")
	@commands.is_owner()
	async def forbidden_commands(self, ctx):

	    embed = discord.Embed(title=f'Owner Only Commands', description='Here are my __OWNER-ONLY__ Modules! Type These In My DMs', colour=0xC0C0C0, timestamp=ctx.message.created_at)

	    embed.add_field(name='Turns off the bot', value="`c!logout`", inline=False)
	    embed.add_field(name='DM Anyone you want.', value="`c!dm <user_id> <message>`", inline=False)
	    embed.add_field(name='Sends The Shard Count.', value="`c!present_shard`", inline=False)
	    embed.add_field(name='Bypass all checks & cooldowns.', value="`c!sudo <command>`", inline=False)
	    embed.add_field(name='Disables a command', value="`c!unload <command>`", inline=False)
	    embed.add_field(name='Enables a disabled command', value="`c!reload <command>`", inline=False)
	    embed.add_field(name='Pushes an Announcement to the Cryptide server for a new release', value="`c!release`", inline=False)
	    embed.add_field(name='Updates the bot', value="`c!update <status or cmd>`", inline=False)
	    embed.add_field(name='Sends a list of servers the bot is in', value="`c!servers`", inline=False)

	    embed.set_footer(text=f"Carpe Noctem | {self.bot.user.name}")
	    embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

	    await ctx.author.send(embed=embed)
	    await ctx.send("I've DM'd You The List!")

	@commands.command()
	async def nsfwexperimental(self, ctx):
	    await ctx.send(akaneko.nsfw.masturbation())

	@commands.command()
	async def rjoke(self, ctx):
		if ctx.channel.is_nsfw():
			titles = ['What do 9 out of 10 people enjoy? \ngang rape :D',
	        	'Rape is such an ugly word, I prefer the term struggle snuggle.',
	        	'I saw a man trying to rape a girl, i decided to help, she didn’t stand a chance against both of us',
	        	'99% of women kiss with their eyes closed, that’s why it’s so hard to identify the rapist.',
	        	'No means no, but if you use chloroform it’s a guaranteed yes.',
	        	'Guy walks into a bar. Sees a hot girl. Walks up to her and says “your getting laid tonight” She replies “what are you some sort of psychic” He says “No i’m just stronger than you”.',
	        	'How can you tell that a pedophile likes music? \nHe rapes D minor',
	        	'If you’re ever bored, just rape an orphan! What’re they gonna do, tell their parents?',
	        	'What’s the hardest thing about losing your virginity? Making sure she doesn’t wake up.',
	        	'Its only rape if she finds out.',
	        	'What do You call a gun that rapes someone? An assault rifle.',
	        	'Consent is just some fucked up feminist propaganda.',
	        	'She said no. So I raped her.']
			await ctx.send(f"{random.choice(titles)}")
		else:
			await ctx.send("HEY! What are you doing??? This isn't an NSFW Channel....")


	@commands.command()
	@commands.is_owner()
	async def present_shard(self, ctx):
	    shard = discord.AutoShardedClient
	    await ctx.send(f"{shard.shards} Is Present")

	@commands.command(name="unload")
	@commands.is_owner()
	async def unload(self, ctx, command_name):
	    command = self.bot.get_command(command_name)
	    command.enabled = False
	    await ctx.send(f"`{command_name}` has been unloaded.")

	@commands.command(name="reload")
	@commands.is_owner()
	async def reload(self, ctx, command_name):
	    command = self.bot.get_command(command_name)
	    command.enabled = True
	    await ctx.send(f"`{command_name}` has been reloaded.")

	@commands.command()
	@commands.is_owner()
	async def release(self, ctx):
	    release_role_id = 827825413706481664
	    release_ping_str = f"<@&{release_role_id}>"

	    questions = [
            [
                "What type of release is this?",
                "1 | Regular Release\n2 | Security Release",
            ],
            ["What version are you releasing?", "\u2009"],
            ["What is the content for this release?", "\u2009"],
        ]
	    answers = [
	        await get_message(self.bot, ctx, question[0], question[1], timeout=500)
	        for question in questions
        ]

	    color_enum = {
            "1": 0x6E6E6E,  # Dark Color
            "2": 0x4D4D4D,  # Even Darker Color
        }
	    color = color_enum.get(answers[0], 0x6E6E6E)

	    tag = answers[1]
	    if "v" not in tag.lower():
	        tag = f"V{tag}"
	    tag = tag.capitalize().replace(" ", "")

	    desc = f"{answers[2]}\n\n------------\nEnjoy :D"

	    embed = discord.Embed(
            title=f"**Bot Release:** `{tag}`",
            description=desc,
            color=color,
            timestamp=ctx.message.created_at,
        )
	    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)

	    if await review_embed(self.bot, ctx, embed):
	        channel = await self.bot.fetch_channel(827772052337328170)
	        await channel.send(release_ping_str, embed=embed)
	        await ctx.send(f"Announcement Sent.")
	    else:
	        await ctx.send("Cancelled.")

def setup(bot):
    bot.add_cog(Forbidden(bot))