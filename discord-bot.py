import discord
from discord.ext import commands
import json
from pathlib import Path
import os

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n---------------------")

client = commands.Bot(command_prefix=".", owner_id=230854079847464960, help_command=None)
secret_file = json.load(open(cwd + '/bot_config/secret.json'))
client.config_token = secret_file['token']
client.cwd = cwd
client.colour_list = [c for c in client.colours.values()]
client.version = '7'
client.colours = {
    'WHITE': 0xFFFFFF,
    'AQUA': 0x1ABC9C,
    'GREEN': 0x2ECC71,
    'BLUE': 0x3498DB,
    'PURPLE': 0x9B59B6,
    'LUMINOUS_VIVID_PINK': 0xE91E63,
    'GOLD': 0xF1C40F,
    'ORANGE': 0xE67E22,
    'RED': 0xE74C3C,
    'NAVY': 0x34495E,
    'DARK_AQUA': 0x11806A,
    'DARK_GREEN': 0x1F8B4C,
    'DARK_BLUE': 0x206694,
    'DARK_PURPLE': 0x71368A,
    'DARK_VIVID_PINK': 0xAD1457,
    'DARK_GOLD': 0xC27C0E,
    'DARK_ORANGE': 0xA84300,
    'DARK_RED': 0x992D22,
    'DARK_NAVY': 0x2C3E50
}


@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.author.send(f'{extension} has been loaded.')


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.author.send(f'{extension} has been unloaded.')


if __name__ == '__main__':
    for file in os.listdir(cwd + "/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            client.load_extension(f'cogs.{file[:-3]}')
    client.run(client.config_token)
