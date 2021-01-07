import discord
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
        choice_list.extend(args)
        if arg_count <= 0:
            await ctx.send("Specify some options to choose randomly.")
        else:
            await ctx.send(f'The random option chosen is {random.choice(choice_list)}')


def setup(client):
    client.add_cog(website(client))
