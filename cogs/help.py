import math

import discord
from discord.ext import commands


class Help_Command(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n---------------------')

    @commands.command(name='help', aliases=['h', 'commands'], description='The help command')
    async def help(self, ctx, cog='1'):
        helpEmbed = discord.Embed(title='Help Commands')
        helpEmbed.set_thumbnail(url=self.client.user.avatar_url)

        cogs = [c for c in self.client.cogs.keys()]
        cogs.remove('backend')
        cogs.remove('Jayden')

        totalPages = math.ceil(len(cogs) / 4)

        cog = int(cog)
        if cog > totalPages or cog < 1:
            await ctx.send(f'Invalid page number: {cog} you spastic cunt. Please pick from {totalPages} pages.')
            return

        helpEmbed.set_footer(
            text=f'<> - Required & [] - Optional | Page {cog} of {totalPages}'
        )

        neededCogs = []
        for i in range(4):
            x = i + (int(cog) - 1) * 4
            try:
                neededCogs.append(cogs[x])
            except IndexError:
                pass

        for cog in neededCogs:
            commandList = ""
            for command in self.client.get_cog(cog).walk_commands():
                if command.hidden:
                    continue

                elif command.parent is not None:
                    continue

                commandList += f"**{command.name}** - *{command.description}*\n"
            commandList += '\n'

            helpEmbed.add_field(name=cog, value=commandList, inline=False)

        await ctx.send(embed=helpEmbed)


def setup(client):
    client.add_cog(Help_Command(client))