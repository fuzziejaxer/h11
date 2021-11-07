import discord
from discord.ext import commands

class clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("File: clear.py Loaded")


    @commands.command(aliases=['cl','delete','purge'])
    @commands.has_permissions(manage_messages = True)
    async def clear(ctx,amount=2):
        await ctx.channel.purge(limit = amount+1)
        emb=discord.Embed(title=f"Cleared {amount} Messages")
        msg=await ctx.channel.send(embed=emb)



def setup(client):
    client.add_cog(clear(client))