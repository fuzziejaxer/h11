import discord
from discord.ext import commands

class avatar(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("File: avatar.py Loaded")

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, member : discord.Member):
        user = ctx.author

        em = discord.Embed(title=f"{member.mention}'s Avatar", colour=user.colour)
        em.add_field(name="image", value=member.avatar_url)
        await ctx.send(embed=em)


def setup(client):
    client.add_cog(avatar(client))