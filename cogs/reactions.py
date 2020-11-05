from datetime import datetime

import discord
from discord import Embed
from discord.ext import commands
import random

numbers = ("1️⃣", "2⃣", "3⃣", "4⃣", "5⃣", "6⃣", "7⃣", "8⃣", "9⃣", "🔟")


class reactions(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.polls = []

    # Cog On Ready
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n---------------------')

    @commands.command(name="createpoll", aliases=["mkpoll", "poll"])
    async def create_poll(self, ctx, question: str, *options):
        if len(options) > 10:
            await ctx.send("You can only supply a maximum of 10 options")
        else:
            embed = Embed(title="Poll",
                          description=question,
                          colour=random.choice(self.client.colour_list),
                          timestamp=datetime.utcnow())

            fields = [("Options", "\n".join([f"{numbers[idx]} {option}" for idx, option in enumerate(options)])
                       , False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            message = await ctx.send(embed=embed)

            for emoji in numbers[:len(options)]:
                await message.add_reaction(emoji)

            self.polls.append((message.channel.id, message.id))

    @commands.command(name="letsgoing", aliases=["lg", "g"])
    async def lets_going(self, ctx):
        big_yes = self.client.get_emoji(773090431416139777)
        big_no = self.client.get_emoji(773090453850423317)
        options = ("Yes", "No")
        yes_no = (big_yes, big_no)
        embed = Embed(title="Lets Going?",
                      description="Will you be available for a lets going?",
                      colour=random.choice(self.client.colour_list),
                      timestamp=datetime.utcnow())

        fields = [("Options", "\n".join([f"{yes_no[idx]} {option}" for idx, option in enumerate(options)]), False)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        lets_going = discord.utils.get(ctx.guild.roles, id=749257590520807455)

        await ctx.send(f'{lets_going.mention}')

        message = await ctx.send(embed=embed)

        for emoji in yes_no[:len(options)]:
            await message.add_reaction(emoji)

        self.polls.append((message.channel.id, message.id))


'''
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id in (poll[1] for poll in self.polls):
            message = await self.client.get_channel(payload.channel_id).fetch_message(payload.message_id)

            for reaction in message.reactions:
                if (not payload.member.bot
                        and payload.member in await reaction.users().flatten()
                        and reaction.emoji != payload.emoji.name):
                    await message.remove_reaction(reaction.emoji, payload.member)
'''


def setup(client):
    client.add_cog(reactions(client))