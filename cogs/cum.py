import discord
from discord.utils import get
from discord.ext import commands
import asyncio
import os


class Misc(commands.Cog):
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
            elif int(args) > 50:
                await ctx.send(
                    f"My balls are only of limited size, to produce '{args}' cummies, i would need to consult"
                    f" with harris to learn how to cum that much.")
        except ValueError:
            await ctx.send(f"Want to try a number next time bucko.")

    @commands.command(name='CUM', aliases=['C'], description='The loud in ear cum command')
    async def CUM(self, ctx, args=None):
        cumcumcum = os.path.abspath('./../discord-bot/SoundEffects/cumcumcum.mp3')
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)

        try:
            if args is None:
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()
                voice.play(discord.FFmpegPCMAudio(cumcumcum), after=lambda: print(f"Playing {cumcumcum}"))
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.2
                await asyncio.sleep(int(7))
                voice.stop()
                await voice.disconnect()
                await discord.Message.delete(ctx.message)
            elif int(args) <= 7:
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()
                voice.play(discord.FFmpegPCMAudio(cumcumcum), after=lambda: print(f"Playing {cumcumcum}"))
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.2
                await asyncio.sleep(int(args))
                voice.stop()
                await voice.disconnect()
                await discord.Message.delete(ctx.message)
            elif int(args) > 7:
                await ctx.send(f"Look, my throat would be sorer than harris on a friday night if i cummed for {args}"
                               f" seconds. Try something less than 7 dickhead.")
                await discord.Message.delete(ctx.message)
        except ValueError:
            await ctx.send(f"You seem a bit slow in the head beacuse '{args}' is not a number.")


def setup(client):
    client.add_cog(Misc(client))
