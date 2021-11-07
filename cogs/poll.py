import discord
from discord.ext import commands

class poll(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("File: poll.py Loaded")

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def poll(self ,ctx,*,message):
        emb=discord.Embed(title=" POLL", description=f"{message}")
        msg=await ctx.channel.send(embed=emb)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')



def setup(client):
    client.add_cog(poll(client))