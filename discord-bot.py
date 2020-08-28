import discord
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
import os

bot = commands.Bot(command_prefix=".")
token = open("token.txt", "r").read()


@bot.command()
async def cum(ctx, args=1):
    emoji = bot.get_emoji(702822392371740684)
    if int(args) <= 50:
        await ctx.send(str(emoji) * args)


@bot.command()
async def mms(ctx, args=0):
    if int(args) <= 10:
        mms_img = os.path.abspath('.//mms/mms' + str(args) + '.png')
        await ctx.send(file=discord.File(mms_img))


@bot.command()
async def slut(ctx, args=None):
    if args is None:
        await ctx.send("Please specify a slut to add")
    else:
        with open('sluts.txt') as f:
            if str(args) in f.read():
                await ctx.send(str(args) + " is already in the slut search.")
            else:
                await slut_txt('sluts.txt', str(args))
                await ctx.send(str(args) + " was added to the sluts.")
                # await instaloader(str(args))


@bot.command()
async def slutlist(ctx):
    f = open('sluts.txt')
    for line in f:
        await ctx.send(line),
    f.close()


async def slut_txt(file_name, slut_to_add):
    with open(file_name, 'a+') as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(str(slut_to_add))


async def change_status():
    await bot.wait_until_ready()

    statuses = cycle(['Fuck my ass', 'Jayden sucks cock', 'Daniel is gay', '.cum', 'Ryiab smells',
                      'Harris is .cum master', '.mms', '.slut'])

    while not bot.is_closed():
        status = next(statuses)
        await bot.change_presence(activity=discord.Game(status))
        await asyncio.sleep(10)


async def change_nick(member: discord.Member, nick):
    await member.edit(nick=nick)


async def change_role_colour_function(role: discord.Role, r, g, b):
    await role.edit(colour=discord.Colour.from_rgb(r, g, b))


async def instaloader(sluts):
    arguments = ' --no-videos --no-video-thumbnails --no-captions --no-metadata-json --no-compress-json ' \
                '--count 5 --filename-pattern {shortcode}_{profile}'
    print('instaloader ' + arguments)
    os.system('instaloader ' + str(sluts) + arguments)


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
        await asyncio.sleep(3600)


async def change_harris():
    await bot.wait_until_ready()
    nicknames = cycle(['Commander Cock', 'Cum Master', 'Cum Cum', 'Cum Slut', 'PurePhoenix', 'Boi Underpant'])
    harris_id = bot.get_user(230854079847464960)
    guild_id = bot.get_guild(368541462188654592)

    for guild in bot.guilds:
        if guild == guild_id:
            for member in guild.members:
                if member == harris_id:
                    harris_name = member

    while not bot.is_closed():
        nickname = next(nicknames)
        await change_nick(harris_name, nickname)
        await asyncio.sleep(20)


async def yoink_sluts():
    await bot.wait_until_ready()
    guild_id = bot.get_guild(368541462188654592)
    channel = bot.get_channel(720218331524890705)

    while not bot.is_closed():

        # await change_nick(harris_name, nickname)

        await asyncio.sleep(21600)


async def change_role_colour():
    await bot.wait_until_ready()

    guild_id = bot.get_guild(368541462188654592)

    r_colours = cycle([255, 255, 255, 155, 0, 0, 0, 0, 0, 155, 255, 255])
    g_colours = cycle([0, 155, 255, 255, 255, 255, 255, 155, 0, 0, 0, 0])
    b_colours = cycle([0, 0, 0, 0, 0, 155, 255, 255, 255, 255, 255, 155])

    for guild in bot.guilds:
        if guild == guild_id:
            role = discord.utils.get(guild_id.roles, name="Homos")
            print(role)

    while not bot.is_closed():
        r_colour = int(next(r_colours))
        g_colour = int(next(g_colours))
        b_colour = int(next(b_colours))

        # print('r: ' + str(r_colour) + ' ' + 'g: ' + str(g_colour) + ' ' + 'b: ' + str(b_colour))
        await change_role_colour_function(role, r_colour, g_colour, b_colour)
        await asyncio.sleep(10)


bot.loop.create_task(change_jayden())
bot.loop.create_task(change_harris())
bot.loop.create_task(change_status())
bot.run(token)
