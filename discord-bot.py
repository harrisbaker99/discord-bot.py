import discord
from discord.ext import commands
from itertools import cycle
import asyncio
import os

client = commands.Bot(
    command_prefix=".",
    owner_id=230854079847464960,
    help_command=None
)
token = open("token.txt", "r").read()


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.author.send(f'{extension} has been loaded.')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.author.send(f'{extension} has been unloaded.')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
