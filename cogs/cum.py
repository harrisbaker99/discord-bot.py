from discord.ext import commands


class Misc_Commands(commands.Cog):
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
            elif int(args) == 69:
                await ctx.send(
                    f"Nice\n                                          "
                    f"{str(emoji)}\n                                    "
                    f"{str(emoji)}{str(emoji)}{str(emoji)}\n                              "
                    f"{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}\n                        "
                    f"{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}"
                    f"\n                  {str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}"
                    f"{str(emoji)}{str(emoji)}{str(emoji)}\n            {str(emoji)}{str(emoji)}{str(emoji)}"
                    f"{str(emoji)}"
                    f"{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}\n"
                    f"      {str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}"
                    f"{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}\n"
                    f"{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}"
                    f"{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}{str(emoji)}"
                )
            elif int(args) > 50 & int(args) != 69:
                await ctx.send(
                    f"My balls are only of limited size, to produce '{args}' cummies, i would need to consult"
                    f" with harris to learn how to cum that much.")
        except ValueError:
            await ctx.send(f"Want to try a number next time bucko.")


def setup(client):
    client.add_cog(Misc_Commands(client))
