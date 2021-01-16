from datetime import datetime
from typing import Optional
import discord
from discord import Embed
from discord.ext import commands
import random


class reactions(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.polls = []

    # Cog On Ready
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n---------------------')

    @commands.command(name="letsgoing", aliases=["lg", "g"])
    async def lets_going(self, ctx, *games: Optional[str]):
        """Pings Lets going role and provide poll in an optional chosen game."""
        arg_count = len(games)
        game_string = ""
        for game in games:
            game_string += game + " "

        big_yes = self.client.get_emoji(773090431416139777)
        big_maybe = self.client.get_emoji(792601596797648926)
        big_no = self.client.get_emoji(773090453850423317)

        options = ("Yes", "Later", "No")
        emoji_options = (big_yes, big_maybe, big_no)
        if arg_count <= 0:
            embed = Embed(title="Lets Going?",
                          description=f"{ctx.author.mention} has asked if you be available for a lets going?",
                          colour=random.choice(self.client.colour_list),
                          timestamp=datetime.utcnow())
        else:
            game_string = game_string[:-1]
            embed = Embed(title=f"Lets Going in {game_string}?",
                          description=f"{ctx.author.mention} has asked if you be available for a lets going?",
                          colour=random.choice(self.client.colour_list),
                          timestamp=datetime.utcnow())

        fields = [("Options", "\n".join([f"{emoji_options[idx]} {option}" for idx, option in enumerate(options)]),
                   False)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        lets_going = discord.utils.get(ctx.guild.roles, id=749257590520807455)

        await ctx.send(f'{lets_going.mention}')

        message = await ctx.send(embed=embed)

        for emoji in emoji_options[:len(options)]:
            await message.add_reaction(emoji)

        self.polls = list((message.channel.id, message.id))

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        big_yes = '773090431416139777'
        big_maybe = '792601596797648926'
        big_no = '773090453850423317'
        user = payload.member
        if payload.guild_id is None:
            return
        else:
            if payload.message_id in self.polls:
                if not payload.member.bot:
                    if str(payload.emoji.id) == big_yes:
                        await self.client.get_channel(payload.channel_id).send(
                            f'{user.mention} has said ***YES*** to the lets going request.')
                        return
                    elif str(payload.emoji.id) == big_maybe:
                        await self.client.get_channel(payload.channel_id).send(
                            f'{user.mention} has said ***LATER*** to the lets going request.')
                        return
                    elif str(payload.emoji.id) == big_no:
                        await self.client.get_channel(payload.channel_id).send(
                            f'{user.mention} has said ***NO*** to the lets going request.')
                        return
                    else:
                        return


def setup(client):
    client.add_cog(reactions(client))
