# -*- coding: utf-8 -*-

"""
Cryptide Fun Cog
~~~~~~~~~~~~~~~~

This Allows Fun Commands That Need/Use Cog Functions To Be Used As An Extension.

:copyright: (c) 2021 Trenton "Kawasaki" G
:terms: No Public Use
:visibilty: Private Cog

"""

#Discord
import discord
from discord.ext import commands

#Others
import random
import nekos
from dadjokes import Dadjoke

class Fun(commands.Cog, name="Fun"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def ask(self, ctx, *, question: str):
	    await ctx.message.delete()
	    msg = await ctx.send("**{}** asks: {}\n============================================".format(ctx.message.author, question.replace("@", "@\u200b")))
	    #await ctx.send("============================================")

	@commands.command()
	async def poll(self, ctx, *, msGG):
		await ctx.message.delete()
		embed=discord.Embed(title="Poll 🎉", description=f"{msGG}")
		msg=await ctx.channel.send(embed=embed)
		await msg.add_reaction('👍')
		await msg.add_reaction('👎')

	@commands.command(pass_context=True)
	async def flip(self, ctx):
		choice = random.randint(1, 2)
		if choice == 1:
			await ctx.channel.send("🌕")
		if choice == 2:
			await ctx.channel.send("🌑")

	@commands.command()
	async def slap(self, ctx, *, tget:discord.Member):
			titles = ['Reeeeeeee',
	        	'BOP!',
	        	'Get beamed',
	        	'dang',
	        	'~slaping sounds~',
	        	'Ouch',
	        	'E Moment',
	        	'-_-',
	        	'just wow. the disrespect ;-;']
			img = nekos.img("slap")
			embed = discord.Embed(title=f"{random.choice(titles)}", description=f"{ctx.author.mention} **slapped** {tget.mention} **silly**.", colour=0xC0C0C0)
			embed.set_image(url=img)
			await ctx.send(embed=embed)

	@commands.command()
	async def tickle(self, ctx, *, tget:discord.Member):
			titles = ['Reeeeeeee',
	        	'BOP!',
	        	'Get beamed',]
			img = nekos.img("tickle")
			embed = discord.Embed(title=f"{random.choice(titles)}", description=f"{ctx.author.mention} **tickled** {tget.mention}.", colour=0xC0C0C0)
			embed.set_image(url=img)
			await ctx.send(embed=embed)

	@commands.command()
	async def poke(self, ctx, *, tget:discord.Member):
			titles = ['Boop',
	        	'Owchie :(',
	        	'~anime poking sound~',]
			img = nekos.img("poke")
			embed = discord.Embed(title=f"{random.choice(titles)}", description=f"{ctx.author.mention} **poked** {tget.mention}.", colour=0xC0C0C0)
			embed.set_image(url=img)
			await ctx.send(embed=embed)

	@commands.command()
	async def feed(self, ctx, *, tget:discord.Member):
			titles = ['Yummy :D',
	        	'Scrumptious!',
	        	'Delicious!',]
			img = nekos.img("feed")
			embed = discord.Embed(title=f"{random.choice(titles)}", description=f"{ctx.author.mention} **feed** {tget.mention}.", colour=0xC0C0C0)
			embed.set_image(url=img)
			await ctx.send(embed=embed)

	@commands.command(aliases=['insult'])
	async def bully(self, ctx, *, tget:discord.Member):
		titles = ['You Walk Like Oswald Cobblepot :penguin:',
				'You look like edward nygma.',
				'I like ya "cut" g',
				'nobody likes you. You are a worthless, useless waste of space.',
				'Fuck off you wanker.',
				'Fuck off you bugger.',
				'You Look Like A Cow.',
				'You are a furry.',
				'Shut up you communist socket.',
				'you probably go "iM tHe cApTaiN nOw". captain looking head ass.',
				'you look like a pie eating shit hound. stfu nerd.',
				'you probably like miraculous. shut up.',
				'"OmG cAt nOiR iS sO cuTe" head ass.',
				"Bruh you're one of those kids who put candy in they soda and call it lean."]
		await ctx.send(f"Yo {tget.mention}, {random.choice(titles)}")

	@commands.command()
	async def djoke(self, ctx):
		dadjokes = Dadjoke()
		await ctx.send(dadjokes.joke)

	@commands.command()
	async def hug(self, ctx, *, tget:discord.Member):
			img = nekos.img("hug")
			embed = discord.Embed(description=f"{ctx.author.mention} **hugged** {tget.mention} **like there was no tomorrow**.", colour=0xC0C0C0)
			embed.set_image(url=img)
			await ctx.send(embed=embed)

	@commands.command()
	async def kiss(self, ctx, *, tget:discord.Member):
			img = nekos.img("kiss")
			embed = discord.Embed(description=f"{ctx.author.mention} **kissed** {tget.mention} **like there was no tomorrow**.", colour=0xC0C0C0)
			embed.set_image(url=img)
			await ctx.send(embed=embed)

	@commands.command(name="dice")
	async def roll_dice(self, Ctx):
		await Ctx.send(f"{Ctx.author.display_name}, you rolled a **{randrange(1, 7)}**!")
		return

	@commands.command(aliases=['8ball'])
	async def _8ball(self, ctx, *, question):
		responses = ['its possible.',
	    'no.',
	    'in a few days.',
	    'probably',
	    'Chance of that happening is zero',
	    'Yes',
	    'Not Really',
	    '-_-',
	    'Try again later. Im very tired.']
		await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

def setup(bot):
    bot.add_cog(Fun(bot))