# -*- coding: utf-8 -*-

"""
Cryptide NSFW Cog
~~~~~~~~~~~~~~~~~

This Allows NSFW Commands That Need/Use Cog Functions To Be Used As An Extension.

:copyright: (c) 2021 Trenton "Kawasaki" G
:terms: No Public Use
:visibilty: Private Cog

"""

#Discord
import discord
from discord.ext import commands

#Others
import nekos
from akaneko import akaneko

class NSFW(commands.Cog, name="NSFW"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command("nsfw")
	async def embed1(self, ctx):

	    embed = discord.Embed(title=f'NSFW', description='Here are my nude Modules! :wink:', colour=0xC0C0C0, timestamp=ctx.message.created_at)

	    embed.add_field(name='Shows a girl masterbating', value="`c!sologirl`", inline=False)
	    embed.add_field(name='Shows a nice blowjob gif', value="`c!blowjob`", inline=False)
	    embed.add_field(name='Shows some anal porn', value="`c!anal`", inline=False)
	    embed.add_field(name='Bdsm ;)', value="`c!bdsm`", inline=False)
	    embed.add_field(name='Shows a picture of pussy', value="`c!pussy`", inline=False)
	    embed.add_field(name='Shows a picture of boobs', value="`c!boobs`", inline=False)
	    embed.add_field(name='Shows some hentai', value="`c!hentai`", inline=False)
	    embed.add_field(name='Shows a picture of nice feet', value="`c!feet`", inline=False)
	    embed.add_field(name='Everything Futanari :)', value="`c!futanari`", inline=False)
	    embed.add_field(name='A nice hentai gif', value="`c!gif`", inline=False)
	    embed.add_field(name='Another hentai command. Its some `cum` :wink: :eyes:', value="`c!cum`", inline=False)
	    embed.add_field(name='Generates an NSFW Avatar.', value="`c!nsfw_avatar`", inline=False)

	    embed.set_footer(text=f"Carpe Noctem | {self.bot.user.name}")
	    embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

	    if ctx.channel.is_nsfw():
	        await ctx.send(embed=embed)
	    else:
	        await ctx.send("HEY! What are you doing??? This isn't an NSFW Channel....")

	@commands.command()
	async def sologirl(self, ctx):
	    if ctx.channel.is_nsfw():
	        img = nekos.img("solog")
	        embed = discord.Embed(description="here my friend.", colour=0xC0C0C0)
	        embed.set_image(url=img)
	        embed.set_footer(text="nekos.life")
	        await ctx.send(embed=embed)
	    else:
	        await ctx.send("You must be fucking retarded if you think this is an NSFW channel.")

	@commands.command()
	async def bdsm(self, ctx):
	    if ctx.channel.is_nsfw():
	        img = nekos.img("spank")
	        embed = discord.Embed(description="here my friend.", colour=0xC0C0C0)
	        embed.set_image(url=img)
	        embed.set_footer(text="nekos.life")
	        await ctx.send(embed=embed)
	    else:
	        await ctx.send("You must be fucking retarded if you think this is an NSFW channel.")

	@commands.command()
	async def blowjob(self, ctx):
	    if ctx.channel.is_nsfw():
	        img = nekos.img("blowjob")
	        embed = discord.Embed(description="here my friend.", colour=0xC0C0C0)
	        embed.set_image(url=img)
	        embed.set_footer(text="nekos.life")
	        await ctx.send(embed=embed)
	    else:
	        await ctx.send("You must be fucking retarded if you think this is an NSFW channel.")

	@commands.command()
	async def futanari(self, ctx):
	    if ctx.channel.is_nsfw():
	        img = nekos.img("futanari")
	        embed = discord.Embed(description="here my friend.", colour=0xC0C0C0)
	        embed.set_image(url=img)
	        embed.set_footer(text="nekos.life")
	        await ctx.send(embed=embed)
	    else:
	        await ctx.send("You must be fucking retarded if you think this is an NSFW channel.")

	@commands.command()
	async def anal(self, ctx):
	    if ctx.channel.is_nsfw():
	        img = nekos.img("anal")
	        embed = discord.Embed(description="here my friend.", colour=0xC0C0C0)
	        embed.set_image(url=img)
	        embed.set_footer(text="nekos.life")
	        await ctx.send(embed=embed)
	    else:
	        await ctx.send("You must be fucking retarded if you think this is an NSFW channel.")

	@commands.command()
	async def pussy(self, ctx):
	    if ctx.channel.is_nsfw():
	        img = nekos.img("pussy")
	        embed = discord.Embed(description="here my friend.", colour=0xC0C0C0)
	        embed.set_image(url=img)
	        embed.set_footer(text="nekos.life")
	        await ctx.send(embed=embed)
	    else:
	        await ctx.send("You must be fucking retarded if you think this is an NSFW channel.")

	@commands.command()
	async def gif(self, ctx):
	    if ctx.channel.is_nsfw():
	        img = nekos.img("solog")
	        embed = discord.Embed(description="here my friend.", colour=0xC0C0C0)
	        embed.set_image(url=img)
	        embed.set_footer(text="nekos.life")
	        await ctx.send(embed=embed)
	    else:
	        await ctx.send("You must be fucking retarded if you think this is an NSFW channel.")

	@commands.command()
	async def cum(self, ctx):
	    if ctx.channel.is_nsfw():
	        img = nekos.img("cum")
	        embed = discord.Embed(description="here my friend.", colour=0xC0C0C0)
	        embed.set_image(url=img)
	        embed.set_footer(text="nekos.life")
	        await ctx.send(embed=embed)
	    else:
	        await ctx.send("You must be fucking retarded if you think this is an NSFW channel.")

	@commands.command()
	async def nsfw_avatar(self, ctx):
	    if ctx.channel.is_nsfw():
	        img = nekos.img("nsfw_avatar")
	        embed = discord.Embed(description="here my friend.", colour=0xC0C0C0)
	        embed.set_image(url=img)
	        embed.set_footer(text="nekos.life")
	        await ctx.send(embed=embed)
	    else:
	        await ctx.send("You must be fucking retarded if you think this is an NSFW channel.")

	@commands.command()
	async def boobs(self, ctx):
	    if ctx.channel.is_nsfw():
	        img = nekos.img("boobs")
	        embed = discord.Embed(description="here my friend.", colour=0xC0C0C0)
	        embed.set_image(url=img)
	        embed.set_footer(text="nekos.life")
	        await ctx.send(embed=embed)
	    else:
	        await ctx.send("You must be fucking retarded if you think this is an NSFW channel.")

	@commands.command()
	async def hentai(self, ctx):
	    if ctx.channel.is_nsfw():
	        img = akaneko.nsfw.hentai()
	        embed = discord.Embed(description="here my friend.", colour=0xC0C0C0)
	        embed.set_image(url=img)
	        embed.set_footer(text="akanekopy")
	        await ctx.send(embed=embed)
	    else:
	        await ctx.send("You must be fucking retarded if you think this is an NSFW channel.")

	@commands.command()
	async def feet(self, ctx):
	    if ctx.channel.is_nsfw():
	        img = nekos.img("feet")
	        embed = discord.Embed(description="here my friend.", colour=0xC0C0C0)
	        embed.set_image(url=img)
	        embed.set_footer(text="nekos.life")
	        await ctx.send(embed=embed)
	    else:
	        await ctx.send("You must be fucking retarded if you think this is an NSFW channel.")

def setup(bot):
    bot.add_cog(NSFW(bot))