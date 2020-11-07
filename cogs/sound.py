import discord
from discord.utils import get
from discord.ext import commands
import platform
import asyncio
import os
import random


class SoundClips(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n---------------------')

    @commands.command(name='CUM', aliases=['C'], description='The loud in ear cum command')
    async def CUM(self, ctx, args=None):
        audio = os.path.abspath('./SoundEffects/cumcumcum.mp3')
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        try:
            if args is None:
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
            elif int(args) <= 7:
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()
                voice.play(discord.FFmpegPCMAudio(audio), after=lambda: print(f"Playing {audio}"))
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
            await ctx.send(f"You seem a bit slow in the head because '{args}' is not a number.")

    @commands.command(name='moan', aliases=['m'], description='The loud in ear moan command')
    async def moan(self, ctx, args=None):
        audio = os.path.abspath('./SoundEffects/moan.mp3')
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        try:
            if args is None:
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
            elif int(args) <= 3:
                if voice and voice.is_connected():
                    await voice.move_to(channel)
                else:
                    voice = await channel.connect()
                voice.play(discord.FFmpegPCMAudio(audio), after=lambda: print(f"Playing {audio}"))
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.2
                await asyncio.sleep(int(args))
                voice.stop()
                await voice.disconnect()
                await discord.Message.delete(ctx.message)
            elif int(args) > 3:
                await ctx.send(f"I can only moan for a maximum of 3 seconds, please save me throat cobba.")
                await discord.Message.delete(ctx.message)
        except ValueError:
            await ctx.send(f"You seem a bit slow in the head because '{args}' is not a number.")

    @commands.command(name='fug', description='Fug ya mum')
    async def moan(self, ctx, args):
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
            await ctx.send(f"You seem a bit slow in the head because '{args}' is not a number.")

    @commands.command(name='cockslam', aliases=['cock', 'slam'], description='Fug ya mum')
    async def moan(self, ctx, args):
        audio = os.path.abspath('./SoundEffects/cockslamyamum.mp3')
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
