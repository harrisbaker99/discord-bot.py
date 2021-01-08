from typing import Optional
from discord import Embed
import random
from discord.utils import get
from discord.ext.menus import MenuPages, ListPageSource
from discord.ext.commands import command
from discord.ext.commands import Cog


colours = {
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
colour_list = [c for c in colours.values()]


def syntax(command):
    cmd_and_aliases = "|".join([str(command), *command.aliases])
    params = []

    for key, value in command.params.items():
        if key not in ("self", "ctx"):
            params.append(f"[{key}]" if "NoneType" in str(value) else f"<{key}>")

    params = " ".join(params)

    return f"`{cmd_and_aliases} {params}`"


class HelpMenu(ListPageSource):
    def __init__(self, ctx, data):
        self.ctx = ctx

        super().__init__(data, per_page=8)

    async def write_page(self, menu, fields=[]):
        offset = (menu.current_page*self.per_page) + 1
        len_data = len(self.entries)
        embed = Embed(title="Help",
                      description="This is a help dialog for the retards.",
                      colour=random.choice(colour_list)
                      )
        embed.set_thumbnail(url=self.ctx.guild.me.avatar_url)
        embed.set_footer(text=f"{offset:,} - {min(len_data, offset+self.per_page-1):,} of {len_data:,} commands.")

        for name, value in fields:
            embed.add_field(name=name, value=value, inline=False)

        return embed

    async def format_page(self, menu, commands):
        fields = []

        for command in commands:
            fields.append((command.help, syntax(command)))

        return await self.write_page(menu, fields)


class Help(Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n---------------------')

    async def cmd_help(self, ctx, command):
        embed = Embed(title=f'{command}',
                      description=syntax(command),
                      colour=random.choice(self.client.colour_list))
        embed.add_field(name="Command Description", value=command.help)
        await ctx.send(embed=embed)

    @command(name='help', aliases=['h', 'commands'])
    async def show_help(self, ctx, cmd: Optional[str]):
        """This is the help command, don't know why you need help about this."""
        if cmd is None:
            menu = MenuPages(source=HelpMenu(ctx, list(self.client.commands)),
                             delete_message_after=True)
            await menu.start(ctx)
        else:
            if command := get(self.client.commands, name=cmd):
                await self.cmd_help(ctx, command)
            else:
                await ctx.send(f'The command {cmd} does not exist.')


def setup(client):
    client.add_cog(Help(client))
