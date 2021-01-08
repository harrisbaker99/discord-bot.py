import platform
import traceback
import discord
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
import random
import os

status = cycle(['Jayden sucking cock', '.help', 'yourmumisgay.com'])


class backend(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Cog On Ready
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n---------------------')
        self.change_status.start()

    # Tasks
    @tasks.loop(seconds=5)
    async def change_status(self):
        await self.client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening,
                                      name=(next(status)),
                                      status='dnd'))

    @commands.command(name='reload')
    @commands.is_owner()
    async def reload(self, ctx, cog=None):
        """Reload all/one of the bots cogs."""
        if not cog:
            # No Cog, means we reload all cogs
            async with ctx.typing():
                embed = discord.Embed(
                    title="Reloading all cogs!",
                    colour=random.choice(self.client.colour_list),
                    timestamp=ctx.message.created_at
                )
                for ext in os.listdir("./cogs/"):
                    if ext.endswith('.py') and not ext.startswith('_'):
                        try:
                            self.client.unload_extension(f'cogs.{ext[:-3]}')
                            self.client.load_extension(f'cogs.{ext[:-3]}')
                            embed.add_field(
                                name=f"Reloaded: {ext}",
                                value='\uFEFF',
                                inline=False
                            )
                        except Exception as e:
                            embed.add_field(
                                name=f"Failed to reload: {ext}",
                                value=str(e),
                                inline=False
                            )
                        await asyncio.sleep(0.5)
                await ctx.send(embed=embed)
        else:
            # reload the specific cog
            async with ctx.typing():
                embed = discord.Embed(
                    title="Reloading specified cog!",
                    colour=random.choice(self.client.colour_list),
                    timestamp=ctx.message.created_at
                )
                ext = f"{cog.lower()}.py"
                if not os.path.exists(f"./cogs/{ext}"):
                    # if the file does not exist
                    embed.add_field(
                        name=f"Failed to reload: {ext}",
                        value="This cog does not exist.",
                        inline=False
                    )
                elif ext.endswith('.py') and not ext.startswith('_'):
                    try:
                        self.client.unload_extension(f'cogs.{ext[:-3]}')
                        self.client.load_extension(f'cogs.{ext[:-3]}')
                        embed.add_field(
                            name=f"Reloaded: {ext}",
                            value='\uFEFF',
                            inline=False
                        )
                    except Exception:
                        desired_trace = traceback.format_exc()
                        embed.add_field(
                            name=f'Failed to reload: {ext}',
                            value=desired_trace,
                            inline=False
                        )
            await ctx.send(embed=embed)

    @reload.error
    async def reload_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("You don't own the bot boss man.")

    @commands.command(name='stats', aliases=['Stats', 'stat'])
    async def stats(self, ctx):
        """
        A useful command that displays bot statistics.
        """
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.client.guilds)
        memberCount = len(set(self.client.get_all_members()))

        embed = discord.Embed(title=f'{self.client.user.name} Stats', description='\uFEFF',
                              color=random.choice(self.client.colour_list),
                              timestamp=ctx.message.created_at)

        embed.add_field(name='Bot Version:', value=self.client.version)
        embed.add_field(name='Python Version:', value=pythonVersion)
        embed.add_field(name='Discord.Py Version', value=dpyVersion)
        embed.add_field(name='Total Guilds:', value=str(serverCount))
        embed.add_field(name='Total Users:', value=str(memberCount))
        embed.add_field(name='Bot Developers:', value="<@230854079847464960>")

        embed.set_footer(text=f"AHHHHHHHHHHHHH | {self.client.user.name}")
        embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(backend(client))
