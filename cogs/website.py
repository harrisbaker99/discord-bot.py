import discord
from discord.ext import commands
import os


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


def setup(client):
    client.add_cog(website(client))
