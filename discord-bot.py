import discord
from discord.ext import commands
from discord.utils import get
from itertools import cycle
import asyncio
import os

bot = commands.Bot(command_prefix=".")
token = open("token.txt", "r").read()
jayden_list = list()


@bot.command()
async def cum(ctx, args=1):
    emoji = bot.get_emoji(702822392371740684)
    if int(args) <= 50:
        await ctx.send(str(emoji) * args)
    await discord.Message.delete(ctx.message)


@bot.command()
async def mms(ctx, args=0):
    if int(args) <= 10:
        mms_img = os.path.abspath('.//mms/mms' + str(args) + '.png')
        await ctx.send(file=discord.File(mms_img))
    await discord.Message.delete(ctx.message)


@bot.command()
async def CUM(ctx):
    cumcumcum = os.path.abspath('.//SoundEffects//cumcumcum.mp3')
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice.play(discord.FFmpegPCMAudio(cumcumcum), after=lambda: print(f"Playing {cumcumcum}"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.2
    await asyncio.sleep(7)
    voice.stop()
    await voice.disconnect()
    await discord.Message.delete(ctx.message)


@bot.command()
async def slut(ctx, *args):
    argcount = len(args)
    if argcount <= 0:
        await ctx.send("Please specify a slut to add")
    elif argcount > 1:
        await ctx.send("Should be only one word you fucking spastic")
    else:
        bigargs = ""
        for elem in args:
            bigargs += elem
        with open('sluts.txt') as f:
            if str(bigargs) in f.read():
                await ctx.send(str(bigargs) + " is already in the slut search.")
            else:
                await slut_txt('sluts.txt', str(bigargs))
                await ctx.send(str(bigargs) + " was added to the sluts.")
                # await instaloader(str(bigargs))


@bot.command()
async def slutlist(ctx):
    filesize = os.path.getsize('sluts.txt')
    if filesize == 0:
        await ctx.send('No sluts are in the slut database.')
    else:
        f = open('sluts.txt')
        for line in f:
            await ctx.send(line),
        f.close()


@bot.command()
async def rmslut(ctx, *args):
    argcount = len(args)
    if argcount <= 0:
        await ctx.send("Please specify a slut to remove")
    elif argcount > 1:
        await ctx.send("Should be only one word you fucking spastic")
    else:
        bigargs = ""
        for elem in args:
            bigargs += elem
        with open('sluts.txt', "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                print(i + bigargs)
                if i != bigargs:
                    f.write(i)
            f.truncate()


@bot.command()
async def jlist(ctx):
    filesize = os.path.getsize('jlist.txt')
    if filesize == 0:
        await ctx.send('No nicknames for the dickhead in the database.')
    else:
        f = open('jlist.txt')
        for line in f:
            await ctx.send(line)
            await asyncio.sleep(0.5)
        f.close()


@bot.command()
async def jgay(ctx, *args):
    argcount = len(args)
    if argcount <= 0:
        await ctx.send("Specify a name for the faggot.")
    else:
        bigargs = ""
        for elem in args:
            bigargs += elem + " "
        bigargs = bigargs[:-1]
        with open('jlist.txt') as f:
            if str(bigargs) in f.read():
                await ctx.send(str(bigargs) + " is already in the dickhead list.")
            else:
                await slut_txt('jlist.txt', str(bigargs))
                await ctx.send(str(bigargs) + " was added to the dickheads list.")
                # await instaloader(str(bigargs))


@bot.command()
async def rmgay(ctx, *args):
    argcount = len(args)
    if argcount <= 0:
        await ctx.send("Please specify a nickname to remove")
    else:
        bigargs = ""
        for elem in args:
            bigargs += elem + " "
        bigargs = bigargs[:-1]
        with open('jlist.txt', "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                print(i + bigargs)
                if i != bigargs:
                    f.write(i)
            f.truncate()


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


async def dickheadarray():
    filesize = os.path.getsize('jlist.txt')
    del jayden_list[:]
    if filesize == 0:
        print(f"The jlist text file is empty.")
    else:
        f = open('jlist.txt')
        for line in f:
            # print(line)
            jayden_list.append(line)
        f.close()


async def change_jayden():
    await bot.wait_until_ready()
    jayden_id = bot.get_user(142933221015945216)

    for guild in bot.guilds:
        for member in guild.members:
            if member == jayden_id:
                jayden_name = member

    while not bot.is_closed():
        await dickheadarray()
        i = 0
        while i < len(jayden_list):
            print(f"Jayden's current nickname is: {jayden_list[i]}.")
            await change_nick(jayden_name, jayden_list[i])
            await asyncio.sleep(21600)
            i += 1


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
            role = discord.utils.get(guild_id.roles, name="Rainbow")

    while not bot.is_closed():
        r_colour = int(next(r_colours))
        g_colour = int(next(g_colours))
        b_colour = int(next(b_colours))
        # print('r: ' + str(r_colour) + ' ' + 'g: ' + str(g_colour) + ' ' + 'b: ' + str(b_colour))
        await change_role_colour_function(role, r_colour, g_colour, b_colour)
        await asyncio.sleep(0.2)


bot.loop.create_task(change_jayden())
bot.loop.create_task(change_harris())
bot.loop.create_task(change_status())
bot.run(token)
