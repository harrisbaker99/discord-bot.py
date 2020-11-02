import traceback
import discord
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
import random
import os

jayden_list = list()
harris_list = list()
status = cycle(['Jayden sucking cock', '.help', 'yourmumisgay.com'])


async def dickheadarray():
    filesize = os.path.getsize('jlist.txt')
    del jayden_list[:]
    if filesize == 0:
        print(f"The jlist text file is empty.")
    else:
        f = open('jlist.txt')
        for line in f:
            jayden_list.append(line)
        f.close()


async def change_nick(member: discord.Member, nick):
    await member.edit(nick=nick)


async def harrisarray():
    filesize = os.path.getsize('hlist.txt')
    del harris_list[:]
    if filesize == 0:
        print(f"The jlist text file is empty.")
    else:
        f = open('hlist.txt')
        for line in f:
            harris_list.append(line)
        f.close()


class backend(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Cog On Ready
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n---------------------')
        self.change_status.start()

    # Tasks
    @tasks.loop(seconds=5)
    async def change_status(self):
        await self.client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening,
                                      name=(next(status)),
                                      status='dnd'))

    @tasks.loop(hours=24)
    async def change_jayden(self):
        await self.client.wait_until_ready()
        jayden_id = self.client.get_user(142933221015945216)

        for guild in self.client.guilds:
            for member in guild.members:
                if member == jayden_id:
                    jayden_name = member
                    while not self.client.is_closed():
                        await dickheadarray()
                        i = 0
                        while i < len(jayden_list):
                            await change_nick(jayden_name, jayden_list[i])
                            i += 1

    @tasks.loop(hours=4)
    async def change_harris(self):
        await self.client.wait_until_ready()
        harris_id = self.client.get_user(230854079847464960)
        guild_id = self.client.get_guild(368541462188654592)

        for guild in self.client.guilds:
            if guild == guild_id:
                for member in guild.members:
                    if member == harris_id:
                        harris_name = member
                        while not self.client.is_closed():
                            await harrisarray()
                            i = 0
                            while i < len(harris_list):
                                await change_nick(harris_name, harris_list[i])
                                i += 1

    # Before Loops for changing nicknames, waiting for the bot to become online first
    ''''@change_jayden.before_loop
    async def before_change_jayden(self):
        await asyncio.sleep(86400)

    @change_harris.before_loop
    async def before_change_harris(self):
        await asyncio.sleep(14400)
    '''

    @commands.command(name='reload', description='Reload all/one of the bots cogs!')
    @commands.is_owner()
    async def reload(self, ctx, cog=None):
        if not cog:
            # No Cog, means we reload all cogs
            async with ctx.typing():
                embed = discord.Embed(
                    title="Reloading all cogs!",
                    colour=random.choice(self.client.colour_list),
                    timestamp=ctx.message.created_at
                )
                for ext in os.listdir("./cogs/"):
                    if ext.endswith('.py') and not ext.startswith('_'):
                        try:
                            self.client.unload_extension(f'cogs.{ext[:-3]}')
                            self.client.load_extension(f'cogs.{ext[:-3]}')
                            embed.add_field(
                                name=f"Reloaded: {ext}",
                                value='\uFEFF',
                                inline=False
                            )
                        except Exception as e:
                            embed.add_field(
                                name=f"Failed to reload: {ext}",
                                value=str(e),
                                inline=False
                            )
                        await asyncio.sleep(0.5)
                await ctx.send(embed=embed)
        else:
            # reload the specific cog
            async with ctx.typing():
                embed = discord.Embed(
                    title="Reloading specified cog!",
                    colour=random.choice(self.client.colour_list),
                    timestamp=ctx.message.created_at
                )
                ext = f"{cog.lower()}.py"
                if not os.path.exists(f"./cogs/{ext}"):
                    # if the file does not exist
                    embed.add_field(
                        name=f"Failed to reload: {ext}",
                        value="This cog does not exist.",
                        inline=False
                    )
                elif ext.endswith('.py') and not ext.startswith('_'):
                    try:
                        self.client.unload_extension(f'cogs.{ext[:-3]}')
                        self.client.load_extension(f'cogs.{ext[:-3]}')
                        embed.add_field(
                            name=f"Reloaded: {ext}",
                            value='\uFEFF',
                            inline=False
                        )
                    except Exception:
                        desired_trace = traceback.format_exc()
                        embed.add_field(
                            name=f'Failed to reload: {ext}',
                            value=desired_trace,
                            inline=False
                        )
            await ctx.send(embed=embed)

    @reload.error
    async def reload_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("You don't own the bot boss man.")


def setup(client):
    client.add_cog(backend(client))
