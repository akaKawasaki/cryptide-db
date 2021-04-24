# -*- coding: utf-8 -*-

"""
Cryptide Moderation Cog
~~~~~~~~~~~~~~~~~~~~~~~

This Allows Moderation Commands That Need/Use Cog Functions To Be Used As An Extension.

:copyright: (c) 2021 Trenton "Kawasaki" G
:terms: No Public Use
:visibilty: Private Cog

"""

#Discord
import discord
from discord.ext import commands

#Jishaku Modules
from jishaku.models import copy_context_with

#Other
from authgen import Generator
import json

class Moderation(commands.Cog, name="Moderation"):
	def __init__(self, bot):
		self.bot = bot
		self.passGene = Generator

	@commands.command(name="sudo")
	@commands.is_owner()
	async def sudo(self, ctx: commands.Context, *, command_string: str):
		alt_ctx = await copy_context_with(ctx, content=ctx.prefix + command_string)

		if alt_ctx.command is None:
			return await ctx.send(f'Command "{alt_ctx.invoked_with}" is not found')

		return await alt_ctx.command.reinvoke(alt_ctx)

	@commands.command()
	async def dm(self, ctx, user_id=None, *, args=None):
	    if user_id != None and args != None:
	        try:
	            target = await self.bot.fetch_user(user_id)
	            await target.send(args)

	            await ctx.channel.send("'" + args + "' sent to: " + target.name)

	        except:
	            await ctx.channel.send("Couldn't dm the given user.")
	    else:
	        await ctx.channel.send("You didn't provide a user's id and/or a message.")

	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member : discord.Member, *, reason=None):
	    await member.kick(reason=reason)
	    await ctx.send(f'{member.mention} was kicked for `{reason}`')

	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member : discord.Member, *, reason=None):
	    await member.ban(reason=reason)
	    await ctx.send(f'{member.mention} was banned for `{reason}`')

	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def unban(ctx, *, member):
	    banned_users = await ctx.guild.bans()
	    member_name, me,member_discrimonator = member.split('#')

	    for ban_entry in banned_users:
	        user = ban_entry.user

	        if (user.name, user.discrimonator) == (member_name, member_discrimonator):
	            await ctx.guild.unban(user)
	            await ctx.send(f'Unbanned {user.mention}')
	            return

	@commands.command(aliases=['prune'])
	@commands.cooldown(1, 90, commands.BucketType.user)
	async def purge(self, ctx, amount=5):
		if amount>999:
			await ctx.send("The message amount must be 999 or below")
		else:
			await ctx.channel.purge(limit=amount)

def setup(bot):
    bot.add_cog(Moderation(bot))