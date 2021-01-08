from datetime import datetime
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

    @commands.command(name='cum', aliases=['c'], description='The soft in text cum command')
    async def cum(self, ctx, args=None):
        emoji = self.client.get_emoji(702822392371740684)
        try:
            if args is None:
                await ctx.send(str(emoji) * 1)
            elif int(args) <= 50:
                await ctx.send(str(emoji) * int(args))
            elif int(args) == 69:
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
            elif int(args) > 50 & int(args) != 69:
                await ctx.send(
                    f"My balls are only of limited size, to produce '{args}' cummies, i would need to consult"
                    f" with harris to learn how to cum that much.")
        except ValueError:
            await ctx.send(f"Want to try a number next time bucko.")

    @commands.command(name='nice', aliases=['n'], description='Nice')
    async def nice(self, ctx, args=None):
        emoji1 = self.client.get_emoji('🇳')
        emoji2 = self.client.get_emoji('🇮')
        emoji3 = self.client.get_emoji('🇨')
        emoji4 = self.client.get_emoji('🇪')
        # emoji1 = self.client.get_emoji(':regional_indicator_n')
        # emoji2 = self.client.get_emoji(':regional_indicator_i:')
        # emoji3 = self.client.get_emoji(':regional_indicator_c:')
        # emoji4 = self.client.get_emoji(':regional_indicator_e:')
        await ctx.send(f"{str(emoji1)} {str(emoji2)} {str(emoji3)} {str(emoji4)} ")
        print(f"{str(emoji1)} {str(emoji2)} {str(emoji3)} {str(emoji4)} ")

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
    async def r6s_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Put in 2 names cobba.")

    @commands.command(name='mms', aliases=['MMS'], description='The martin minge scale command')
    async def mms(self, ctx, args=None):
        try:
            if args is None:
                mms_img = os.path.abspath('.//mms/mms0.png')
                await ctx.send(file=discord.File(mms_img))
            if int(args) <= 10:
                mms_img = os.path.abspath('.//mms/mms' + str(args) + '.png')
                await ctx.send(file=discord.File(mms_img))
            elif 10 < int(args) <= 100:
                await ctx.send("You seem to be just a tad minged, this is the best i can do sport.")
                mms_img = os.path.abspath('.//mms/mms10.png')
                await ctx.send(file=discord.File(mms_img))
            elif int(args) > 100:
                await ctx.send("Holy fuck, you sir, are quite minged. I don't have a scale that goes that high, "
                               "have this instead champ.")
                mms_img = os.path.abspath('.//mms/mms10.png')
                await ctx.send(file=discord.File(mms_img))
        except ValueError:
            await ctx.send(f"You seem a bit slow in the head because '{args}' is not a number.")


def setup(client):
    client.add_cog(Misc_Commands(client))
