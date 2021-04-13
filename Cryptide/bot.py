"""
Cryptide Discord Bot
~~~~~~~~~~~~~~~~~~~~

This is a public multipurpose discord bot.

:copyright: (c) 2021 Trenton "Kawasaki" G
:terms: Not Open-Sourced
:visibilty: Public Bot

"""

#Discord-Related
import discord
from discord.ext import commands
from discord.ext.commands import Bot

#Other
import json
from pathlib import Path
import pyfiglet as generate_banner
from PYLog import PYLog
from colorama import *
import asyncio

#Define Banner
ascii_banner = generate_banner.figlet_format("       Cryptide") 

#Define Path
cwd = Path(__file__).parents[0]
cwd = str(cwd)

#Prints
print(Fore.BLUE + Style.BRIGHT + ascii_banner)
print(Fore.GREEN + Style.BRIGHT + "**********************************************************")
print(Fore.YELLOW + Style.BRIGHT + "Cogs initialized")

#Intents
rich_presence = discord.Intents.all()
"""
rich_presence.members = True
rich_presence.messages = True
rich_presence.reactions = True
rich_presence.guilds = True
rich_presence.integrations = True
rich_presence.webhooks = True
rich_presence.bans = True
rich_presence.invites = True
rich_presence.presences = True
"""

init() #windows

#Defining The Client
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('c!', '--', 'c/', 'c$', 'c.', 'c~'),
    case_insensitive=True,
    intents=rich_presence,
    help_command=None,
    description="A complex but yet simplistic discord bot."
)

#Defining Help Pages
imageUrl = "https://cdn.discordapp.com/avatars/811349622709944390/f6758797b79627f4ecf3bc98ecbc6e09.webp?size=1024"

page1 = discord.Embed(title="Page 1/5 | About", description="I am a multipurpose bot with the everything your server will ever need! I come with an antispam module, Many interactive commands, Many misc commands, Many moderation commands, and just so much more for you to enjoy :D\n\nFor a list of commands, type one of the listed options.\n`c!commands`\n`c!cmds`\n`c!cmdlist`", color=0xC0C0C0)
page1.set_thumbnail(url=imageUrl)
page2 = discord.Embed(title="Page 2/5 | Updates", description="If you would like to see any sneek peaks or updates on the bot, [Click Me](https://discord.gg/8JuseZMjzf) and join the updates server! Also, If the bot goes offline, the bot is updating or it is going through a daily examination. This allows us to find bugs.", color=0xC0C0C0)
page2.set_thumbnail(url=imageUrl)
page3 = discord.Embed(title="Page 3/5 | Errors", description="**• __Section 1 - DM's__**\nSome commands require people to have their dms on. You must have them on for these to work.\n\n**• __Section 2 - Authorization__**\nSome commands require people to have the correct permission(s). Make sure they have the permission(s) required. Also, the bot may also be missing a specific permission(s). Please give the bot the permission(s) that it needs or just give it administrator. Whatever suits you.\n\n**• __Section 3 - Connection__**\nSometimes, the bot might not work depending on the [latency/ping](https://blog.stackpath.com/latency/) of the bot, the bot creator, or the bot user (`you`). Please make sure your connection is at least, semi-stable.\n\n**• __Section 4 - Common Sense/Recap In a Nutshell__**\nNow come on. Some things can be explained. If you get an error from the bot itself, it'll tell you. If the bot is offline, it is being examined or updated. If it doesn't respond right away, either [Discord's API](https://discord.com/developers/docs/intro) is having connection problems or there are other [connectivity](https://www.google.com/search?q=what+is+connectivity&rlz=1C1RXQR_enUS935US935&oq=what+is+connectivity&aqs=chrome..69i57j0l9.6502j0j4&sourceid=chrome&ie=UTF-8) issues. Also make sure you've restarted your computer consistently (`after use`) to make sure everything is working as intended.", color=0xC0C0C0)
page3.set_thumbnail(url=imageUrl)
page4 = discord.Embed(title="Page 4/5 | Prefixes", description="I a few prefixes. For context, a `prefix` is something used to `invoke`/`call` a command specified after the `prefix`. Here are my prefixes.\n\n`c!`\n`--`\n<@811349622709944390>\n`c/`\n`c$`\n`c.`\n`c~`", color=0xC0C0C0)
page4.set_thumbnail(url=imageUrl)
page5 = discord.Embed(title="Page 5/5 | Contact", description="If you have any issues or encounter any bugs, Contact me at one of the following handles.\n\nDiscord: <@786334287968337981>\nInstagam: `trenton.was.taken`\nor go into the bug report channel in the [Cryptide Updates](https://discord.gg/8JuseZMjzf) Server", color=0xC0C0C0)
page5.set_thumbnail(url=imageUrl)

bot.helps = [page1, page2, page3, page4, page5]

#Defining Error Responses
bot.responseMessages = {
  "member_not_found": "Member \"{0}\" doesn't exist, {1}.",
  "command_not_found": "Command \"{0}\" doesn't exist, {1}.",
  "command_disabled": "Command \"{0}\" is disabled, {1}.",
  "missing_args": "You are missing required arguments, {}",
  "secret_error": "You managed to bypass all the error checks we had and got this error. I'm suprised. {}.. Well done.",
  "int_not_str": "Argument {0} requires an int, not a str, {1}",
  "str_not_int": "Argument {0} requires a str, not an int, {1}",
  "value_error": "One of the arguments you provided is invalid, {}",
  "permission_error": "I'm Missing Permissions {1}"
}

#Defining Our Token
secret_file = json.load(open(cwd+'/__config__/secrets.json'))
bot.token = secret_file['token']

#Defining The Cogs
bot.Modules = [
        
        #Info
        "__modules__.Misc", #Most Events/Listeners Are Here | Misc Commands
        "__modules__.Help", #Help Commands
        "__data__.Docs", #Holds The RTFM Command. Not about to mess uo my other cogs. So It has its own cog file.

        #Experimental
        "__modules__.Forbidden", #Owner/Test Commands

        #Moderation
        "jishaku", #A Useful Cog
        "__modules__.Mod", #Moderation/Enforcement Commands
        "__automod__.Antispam", #AntiSpam Module

        #Regular
        "__modules__.NSFW", #NSFW/18+ Commands
        "__modules__.Fun", #Fun/Playful Commands
        "__modules__.EasterEggs", #Secret/Covert/Hidden Commands
]

#Load The Cogs
for x in bot.Modules:
    bot.load_extension(x)

#Non-Converted Listeners
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
      commandname = ctx.invoked_with
      cname = commandname.split(".")[0]
      print(cname)
      if cname.isdigit():
        e = PYLog.mode("error")
        PYLog.log(e, "Command called was an integer.")
      else:
        await ctx.send(bot.responseMessages["command_not_found"].format(commandname,ctx.author.name))
    elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(bot.responseMessages["missing_args"].format(ctx.author.name))
    elif isinstance(error, commands.BotMissingPermissions):
      await ctx.send(bot.responseMessages["permission_error"].format(ctx.author.name))
    elif isinstance(error, commands.DisabledCommand):
      cname = ctx.invoked_with
      await ctx.send(bot.responseMessages["command_disabled"].format(cname, ctx.author.name))
    elif isinstance(error, commands.MemberNotFound):
      args = ctx.message.content.split(" ")[0:]
      m = args[1]
      await ctx.send(bot.responseMessages["member_not_found"].format(m, ctx.author.name))
    elif isinstance(error, ValueError):
      await ctx.send(bot.responseMessages["value_error"].format(ctx.author.name))
    else:
      e = PYLog.mode("error")
      PYLog.log(e, error)

@bot.event
async def on_message(message):
    #ignore yourselves
    if message.author.id == bot.user.id:
        return

    await bot.process_commands(message)

@bot.command("update")
@commands.is_owner()
async def updateCommands(ctx):
    embed = discord.Embed(description="Bot has been updated :D", color=0xC0C0C0)
    await ctx.send(embed=embed)
    print("Bot has been update :D")
    for x in bot.Modules:
        bot.reload_extension(x)


@bot.command()
async def help(ctx):
    buttons=[u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"]
    current=0

    msg = await ctx.send(embed=bot.helps[current])
    
    for button in buttons:
        await msg.add_reaction(button)
        
    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=90000000000000000000000000000000000000000000000000000000000000000.0)

        except asyncio.TimeoutError:
            return print("This Is useless, But The New Help Command Needs It...")

        else:
            previous_page = current
            if reaction.emoji == u"\u23EA":
                current = 0
                
            elif reaction.emoji == u"\u2B05":
                if current > 0:
                    current -= 1
                    
            elif reaction.emoji == u"\u27A1":
                if current < len(bot.helps)-1:
                    current += 1

            elif reaction.emoji == u"\u23E9":
                current = len(bot.helps)-1

            for button in buttons:
                await msg.remove_reaction(button, ctx.author)

            if current != previous_page:
                await msg.edit(embed=bot.helps[current])

#Functions
def read_json(filename):
    with open(f"{cwd}/__config__/{filename}.json", "r") as file:
        data = json.load(file)
    return data

def write_json(data, filename):
    with open(f"{cwd}/__config__/{filename}.json", "w") as file:
        json.dump(data, file, indent=4)

bot.run(bot.token)