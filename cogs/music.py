import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n---------------------')

    @commands.command(name='play', aliases=['p'])
    async def play(self, ctx, url: str):
        """I play a song. I only can use youtube links."""
        song_there = os.path.isfile('song.mp3')
        try:
            if song_there:
                os.remove('song.mp3')
        except PermissionError:
            await ctx.send("Wait for me to finish what im doing. Or you can stop me.")

        voiceChannel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(voiceChannel)
        else:
            voice = await voiceChannel.connect()

        ydl_opts = {
            'format': 'bestaudio',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        for file in os.listdir('./'):
            if file.endswith('.mp3'):
                os.rename(file, 'song.mp3')

        voice.play(discord.FFmpegPCMAudio('song.mp3'))

    @commands.command(name='leave', aliases=['l'])
    async def leave(self, ctx):
        """I leave the voice channel. I undertand that i can be annoying at times."""
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("I am not connected to a channel. Leave me the fuck alone.")

    @commands.command(name='pause')
    async def pause(self, ctx):
        """I pause the currently playing music."""
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("Im not saying anything right now. Leave me the fuck alone.")

    @commands.command(name='resume')
    async def resume(self, ctx):
        """I resume the current song that was paused."""
        voice = get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("Im already talking or you told me to fucking stop.")

    @commands.command(name='stop')
    async def stop(self, ctx):
        """I stop the current song. I will need a new youtube link after this."""
        voice = get(self.client.voice_clients, guild=ctx.guild)
        voice.stop()


def setup(client):
    client.add_cog(Music(client))
