from discord.ext import commands
import os


async def add_txt(file_name, txt_to_add):
    with open(file_name, 'a+') as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(str(txt_to_add))


class Jayden(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog has been loaded\n---------------------')

    @commands.command(name='jlist', description='Show jaydens nicknames.')
    async def jlist(self, ctx):
        filesize = os.path.getsize('jlist.txt')
        if filesize == 0:
            await ctx.send('No nicknames for the dickhead in the database.')
        else:
            f = open('jlist.txt')
            jaydenArray = ""
            for line in f:
                jaydenArray += line
            await ctx.send(jaydenArray)
            f.close()

    @commands.command(name='jgay', description='Add a nickname for the retard.')
    async def jgay(self, ctx, *args):
        argcount = len(args)
        if argcount <= 0:
            await ctx.send("Specify a name for the faggot.")
        else:
            bigargs = ""
            for elem in args:
                bigargs += elem + " "
            bigargs = bigargs[:-1]
            with open('jlist.txt') as f:
                if str(bigargs) in f.read():
                    await ctx.send(str(bigargs) + " is already in the dickhead list.")
                else:
                    await add_txt('jlist.txt', str(bigargs))
                    await ctx.send(str(bigargs) + " was added to the dickheads list.")


def setup(client):
    client.add_cog(Jayden(client))
