from datetime import datetime
from typing import Optional
import discord
from discord import Embed
from discord.ext import commands
import os
import random


class Misc_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n---------------------')

    @commands.command(name='cum', aliases=['c'])
    async def cum(self, ctx, amount: Optional[int]):
        """This command sends the cummies. No number will send a default 1 Cum."""
        emoji = self.client.get_emoji(702822392371740684)
        try:
            if amount is None:
                await ctx.send(str(emoji) * 1)
            elif int(amount) <= 50:
                await ctx.send(str(emoji) * int(amount))
            elif int(amount) == 69:
                await ctx.send(
                    f"Nice\n                                          "
                    f"{str(emoji)}\n                                    "
                    f"{str(emoji)}{str(emoji)}{str(emoji)}\n                              "
                    f"{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}\n                        "
                    f"{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}"
                    f"\n                  {str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}"
                    f"{str(emoji)}{str(emoji)}{str(emoji)}\n            {str(emoji)}{str(emoji)}{str(emoji)}"
                    f"{str(emoji)}"
                    f"{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}\n"
                    f"      {str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}"
                    f"{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}\n"
                    f"{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}"
                    f"{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}"
                )
            elif int(amount) > 50 & int(amount) != 69:
                await ctx.send(
                    f"My balls are only of limited size, to produce '{amount}' cummies, i would need to consult"
                    f" with harris to learn how to cum that much.")
        except ValueError:
            await ctx.send(f"Want to try a number next time bucko.")

    @commands.command(
        name='website',
        aliases=['web', 'w']
    )
    async def website(self, ctx):
        """This displays a qr code and url for my website."""
        website_img = os.path.abspath('./images/gaymum.com.png')
        await ctx.send(file=discord.File(website_img))
        await ctx.send('https://yourmumisgay.com')

    @commands.command(
        name='faggot',
        aliases=['fag', 'DSL', 'dsl', 'FAG', 'Faggot']
    )
    async def faggot(self, ctx):
        """This displays an image of the faggot."""
        website_img = os.path.abspath('./images/faggot.jpg')
        await ctx.send(file=discord.File(website_img))

    @commands.command(
        name='jayden',
        aliases=['gayden', 'gay']
    )
    async def jayden(self, ctx):
        """This displays an image of our gay acquaintance."""
        website_img = os.path.abspath('./images/jaydengay.png')
        await ctx.send(file=discord.File(website_img))

    @commands.command(
        name='random',
        aliases=['r', 'choice']
    )
    async def random(self, ctx, *options: Optional[str]):
        """Will choose a random option from your specified list or from a games list"""
        arg_count = len(options)
        choice_list = list()
        games = list(['Rocket League', 'Rainbow 6 Siege', 'Zombies', 'War-zone', 'Your Mum'])
        choice_list.extend(options)
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
        aliases=['r6', 'death', 'prank']
    )
    async def r6s(self, ctx, player1: str, player2: str):
        """Chooses if player 1 kills player 2 or not."""

        num = random.random()

        if num <= 0.5:
            embed = Embed(title="Ouch",
                          description=f"***{player1}*** gets to shoot ***{player2}*** this round.",
                          colour=random.choice(self.client.colour_list),
                          timestamp=datetime.utcnow())
            await ctx.send(embed=embed)
        else:
            embed = Embed(title="Wow Rigged",
                          description=f"***{player1}*** does not get to shoot ***{player2}*** this round.",
                          colour=random.choice(self.client.colour_list),
                          timestamp=datetime.utcnow())
            await ctx.send(embed=embed)

    @r6s.error
    async def r6s_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Put in 2 names cobba.")

    @commands.command(name='mms', aliases=['MMS'])
    async def mms(self, ctx, value: Optional[int] = None):
        """The official martin minge scale command."""
        try:
            if value is None:
                mms_img = os.path.abspath('.//mms/mms0.png')
                await ctx.send(file=discord.File(mms_img))
            if int(value) <= 10:
                mms_img = os.path.abspath('.//mms/mms' + str(value) + '.png')
                await ctx.send(file=discord.File(mms_img))
            elif 10 < int(value) <= 100:
                await ctx.send("You seem to be just a tad minged, this is the best i can do sport.")
                mms_img = os.path.abspath('.//mms/mms10.png')
                await ctx.send(file=discord.File(mms_img))
            elif int(value) > 100:
                await ctx.send("Holy fuck, you sir, are quite minged. I don't have a scale that goes that high, "
                               "have this instead champ.")
                mms_img = os.path.abspath('.//mms/mms10.png')
                await ctx.send(file=discord.File(mms_img))
        except ValueError:
            await ctx.send(f"You seem a bit slow in the head because '{value}' is not a number.")

    @commands.command(
        name='hung',
        aliases=['fat', 'cock', 'fatcock']
    )
    async def fat_cock(self, ctx):
        """This displays an image of the god himself."""
        fat_cock = os.path.abspath('./images/hung-fat-daddy-fat-cock.png')
        await ctx.send(file=discord.File(fat_cock))


def setup(client):
    client.add_cog(Misc_Commands(client))
