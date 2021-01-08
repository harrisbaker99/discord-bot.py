from typing import Optional
import discord
from discord.utils import get
from discord.ext import commands
import asyncio
import os


class SoundClips(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n---------------------')

    @commands.command(name='CUM', aliases=['C'])
    async def CUM(self, ctx, seconds: Optional[int] = None):
        """The loud in ear cum command."""
        audio = os.path.abspath('./SoundEffects/cumcumcum.mp3')
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        try:
            if seconds is None:
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()
                voice.play(discord.FFmpegPCMAudio(audio), after=lambda: print(f"Playing {audio}"))
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.2
                await asyncio.sleep(int(7))
                voice.stop()
                await voice.disconnect()
                await discord.Message.delete(ctx.message)
            elif int(seconds) <= 7:
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()
                voice.play(discord.FFmpegPCMAudio(audio), after=lambda: print(f"Playing {audio}"))
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.2
                await asyncio.sleep(int(seconds))
                voice.stop()
                await voice.disconnect()
                await discord.Message.delete(ctx.message)
            elif int(seconds) > 7:
                await ctx.send(f"Look, my throat would be sorer than harris on a friday night if i cummed for {seconds}"
                               f" seconds. Try something less than 7 dickhead.")
                await discord.Message.delete(ctx.message)
        except ValueError:
            await ctx.send(f"You seem a bit slow in the head because '{seconds}' is not a number.")

    @commands.command(name='moan', aliases=['m'])
    async def moan(self, ctx, seconds: Optional[int] = None):
        """The loud in ear moan command."""
        audio = os.path.abspath('./SoundEffects/moan.mp3')
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        try:
            if seconds is None:
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()
                voice.play(discord.FFmpegPCMAudio(audio), after=lambda: print(f"Playing {audio}"))
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.2
                await asyncio.sleep(int(3))
                voice.stop()
                await voice.disconnect()
                await discord.Message.delete(ctx.message)
            elif int(seconds) <= 3:
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()
                voice.play(discord.FFmpegPCMAudio(audio), after=lambda: print(f"Playing {audio}"))
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.2
                await asyncio.sleep(int(seconds))
                voice.stop()
                await voice.disconnect()
                await discord.Message.delete(ctx.message)
            elif int(seconds) > 3:
                await ctx.send(f"I can only moan for a maximum of 3 seconds, please save me throat cobba.")
                await discord.Message.delete(ctx.message)
        except ValueError:
            await ctx.send(f"You seem a bit slow in the head because '{seconds}' is not a number.")

    @commands.command(name='fug')
    async def fug(self, ctx, seconds=None):
        """Fug ya mum."""
        audio = os.path.abspath('./SoundEffects/fugyamum.mp3')
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        try:
            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(audio), after=lambda: print(f"Playing {audio}"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.2
            await asyncio.sleep(int(3))
            voice.stop()
            await voice.disconnect()
            await discord.Message.delete(ctx.message)
        except ValueError:
            await ctx.send(f"You seem a bit slow in the head because '{seconds}' is not a number.")

    @commands.command(name='cumslam', aliases=['slam'])
    async def cumslam(self, ctx, args=None):
        """Cum slam ya mum."""
        audio = os.path.abspath('./SoundEffects/cumslamyamum.mp3')
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        try:
            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(audio), after=lambda: print(f"Playing {audio}"))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.2
            await asyncio.sleep(int(3))
            voice.stop()
            await voice.disconnect()
            await discord.Message.delete(ctx.message)
        except ValueError:
            await ctx.send(f"You seem a bit slow in the head because '{args}' is not a number.")


def setup(client):
    client.add_cog(SoundClips(client))
