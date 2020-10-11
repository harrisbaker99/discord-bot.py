import discord
from discord.ext import commands
import os


class MMS_Command(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n---------------------')

    @commands.command(name='mms', aliases=['MMS'], description='The martin minged scale command')
    async def mms(self, ctx, args=None):
        try:
            if args is None:
                mms_img = os.path.abspath('.//mms/mms0.png')
                await ctx.send(file=discord.File(mms_img))
            if int(args) <= 10:
                mms_img = os.path.abspath('.//mms/mms' + str(args) + '.png')
                await ctx.send(file=discord.File(mms_img))
            elif int(args) > 10:
                await ctx.send("You seem to be just a tad minged, this is the best i can do sport.")
                mms_img = os.path.abspath('.//mms/mms10.png')
                await ctx.send(file=discord.File(mms_img))
        except ValueError:
            await ctx.send(f"You seem a bit slow in the head beacuse '{args}' is not a number.")


def setup(client):
    client.add_cog(MMS_Command(client))
