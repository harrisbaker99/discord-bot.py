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


# 142933221015945216


async def jayden():
    gayden = bot.get_user(142933221015945216)
    if gayden:
        await bot.user.edit(id=142933221015945216, nick='cock')
        print(bot.get_user(142933221015945216))
    else:
        print("the fuck am i doing")


async def change_status():
    await bot.wait_until_ready()

    statuses = cycle(['Fuck my ass', 'Jayden sucks cock', 'Daniel is gay', '.cum', 'Ryiab smells',
                      'Harris is .cum master'])

    while not bot.is_closed():
        status = next(statuses)

        await bot.change_presence(activity=discord.Game(status))

        await asyncio.sleep(10)


async def change_jayden():
    await bot.wait_until_ready()
    nicknames = cycle(['Big Dickhead', 'CockSucker'])

    while not bot.is_closed():
        nickname = next(nicknames)

        await jayden()

        await asyncio.sleep(10)


# bot.loop.create_task(change_jayden())
bot.loop.create_task(change_status())
bot.run(token)
