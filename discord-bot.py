import discord
from discord.ext import commands, tasks
from itertools import cycle
import asyncio

bot = commands.Bot(command_prefix=".")
token = open("token.txt", "r").read()


@bot.command()
async def cum(ctx, args=1):
    emoji = bot.get_emoji(702822392371740684)
    if int(args) <= 50:
        await ctx.send(str(emoji) * args)


async def change_status():
    await bot.wait_until_ready()

    statuses = cycle(['Fuck my ass', 'Jayden sucks cock', 'Daniel is gay', '.cum', 'Ryiab smells',
                      'Harris is .cum master'])

    while not bot.is_closed():
        status = next(statuses)

        await bot.change_presence(activity=discord.Game(status))

        await asyncio.sleep(10)


async def change_nick(member: discord.Member, nick):
    await member.edit(nick=nick)


async def change_jayden():
    await bot.wait_until_ready()
    nicknames = cycle(['Big Dickhead', 'CockSucker', 'Fucktard', 'Wankstick', 'Retard', 'Spastic Cunt'])

    jayden_id = bot.get_user(142933221015945216)

    for guild in bot.guilds:
        for member in guild.members:
            if member == jayden_id:
                jayden_name = member

    while not bot.is_closed():
        nickname = next(nicknames)

        await change_nick(jayden_name, nickname)

        await asyncio.sleep(43200)


async def change_harris():
    await bot.wait_until_ready()
    nicknames = cycle(['Commander Cock', 'Cum Master', 'Cum Cum', 'Cum Slut', 'PurePhoenix'])

    harris_id = bot.get_user(230854079847464960)

    for guild in bot.guilds:
        for member in guild.members:
            if member == harris_id:
                harris_name = member

    while not bot.is_closed():
        nickname = next(nicknames)

        await change_nick(harris_name, nickname)

        await asyncio.sleep(20)


bot.loop.create_task(change_jayden())
bot.loop.create_task(change_status())
bot.run(token)
