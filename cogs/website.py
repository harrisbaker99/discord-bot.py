from datetime import datetime
import discord
from discord import Embed
from discord.ext import commands
import os
import random


class website(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n---------------------')

    @commands.command(
        name='website',
        aliases=['web', 'w'],
        description='Display QR Code for the your mum is gay website'
    )
    async def website(self, ctx):
        website_img = os.path.abspath('./images/gaymum.com.png')
        await ctx.send(file=discord.File(website_img))
        await ctx.send('https://yourmumisgay.com')

    @commands.command(
        name='faggot',
        aliases=['fag', 'DSL', 'dsl', 'FAG', 'Faggot'],
        description='Display a picture of the DSL faggot'
    )
    async def faggot(self, ctx):
        website_img = os.path.abspath('./images/faggot.jpg')
        await ctx.send(file=discord.File(website_img))

    @commands.command(
        name='jayden',
        aliases=['gayden', 'gay'],
        description='Display a picture of gayden sucking some cock'
    )
    async def jayden(self, ctx):
        website_img = os.path.abspath('./images/jaydengay.png')
        await ctx.send(file=discord.File(website_img))

    @commands.command(
        name='random choice',
        aliases=['r', 'random', 'choice'],
        description='Chooses a random choice from a list you provide'
    )
    async def random(self, ctx, *args):
        arg_count = len(args)
        choice_list = list()
        games = list(['Rocket League', 'Rainbow 6 Siege', 'Zombies', 'War-zone', 'Your Mum'])
        choice_list.extend(args)
        if arg_count <= 0:
            embed = Embed(title="Ooga Booga",
                          description=f"The random option chosen is ***{random.choice(games)}***",
                          colour=random.choice(self.client.colour_list),
                          timestamp=datetime.utcnow())
            await ctx.send(embed=embed)
        else:
            embed = Embed(title="Ooga Booga",
                          description=f"The random option chosen is ***{random.choice(choice_list)}***",
                          colour=random.choice(self.client.colour_list),
                          timestamp=datetime.utcnow())
            await ctx.send(embed=embed)

    @commands.command(
        name='R6S',
        aliases=['r6', 'death', 'prank'],
        description='Chooses who kills who'
    )
    async def r6s(self, ctx, arg1, arg2):
        player_1 = str(arg1)
        player_2 = str(arg2)

        num = random.random()

        if num <= 0.5:
            embed = Embed(title="Ouch",
                          description=f"***{player_1}*** gets to shoot ***{player_2}*** this round.",
                          colour=random.choice(self.client.colour_list),
                          timestamp=datetime.utcnow())
            await ctx.send(embed=embed)
        else:
            embed = Embed(title="Wow Rigged",
                          description=f"***{player_1}*** does not get to shoot ***{player_2}*** this round.",
                          colour=random.choice(self.client.colour_list),
                          timestamp=datetime.utcnow())
            await ctx.send(embed=embed)

    @r6s.error
    async def reload_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Put in 2 names cobba.")


def setup(client):
    client.add_cog(website(client))
