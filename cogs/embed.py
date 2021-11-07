import discord
from discord.ext import commands

class embed(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("File: embed.py Loaded")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def embed(self, ctx, title, channel: discord.TextChannel,*,msg):
        user = ctx.author

        emb = discord.Embed(title=f"{title}", description=f"{msg}", colour=user.colour)
        msg = await channel.send(embed=emb)





def setup(client):
    client.add_cog(embed(client))