import discord
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
import os

jayden_list = list()
harris_list = list()
status = cycle(['Fuck my ass', 'Jayden sucks cock', 'Daniel is gay', '.cum', 'Ryiab smells',
                'Harris is .cum master', '.mms', '.slut', 'with Airfried Meatpies'])


class backend(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.change_status.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n---------------------')

    async def change_nick(self, member: discord.Member, nick):
        await member.edit(nick=nick)

    async def dickheadarray(self):
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

    async def harrisarray(self):
        filesize = os.path.getsize('hlist.txt')
        del harris_list[:]
        if filesize == 0:
            print(f"The jlist text file is empty.")
        else:
            f = open('hlist.txt')
            for line in f:
                # print(line)
                harris_list.append(line)
            f.close()

    # Tasks
    @tasks.loop(seconds=10.0)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(next(status)))

    @change_status.before_loop
    async def before_change_status(self):
        await self.client.wait_until_ready()

    @tasks.loop(hours=24)
    async def change_jayden(self):
        await self.client.wait_until_ready()
        jayden_id = self.client.get_user(142933221015945216)

        for guild in self.client.guilds:
            for member in guild.members:
                if member == jayden_id:
                    jayden_name = member

        while not self.client.is_closed():
            await self.dickheadarray()
            i = 0
            while i < len(jayden_list):
                await self.change_nick(jayden_name, jayden_list[i])
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
            await self.harrisarray()
            i = 0
            while i < len(harris_list):
                await self.change_nick(harris_name, harris_list[i])
                i += 1

    @change_jayden.before_loop
    async def before_change_jayden(self):
        await asyncio.sleep(86400)

    @change_harris.before_loop
    async def before_change_harris(self):
        await asyncio.sleep(14400)


def setup(client):
    client.add_cog(backend(client))
