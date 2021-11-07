import discord
from discord.ext import commands

class kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("File: kick.py Loaded")


    @commands.command()
    async def kick(self, ctx, member : discord.Member,*,reason= "No Reason Provided"):
        emb=discord.Embed(title=f"User {member.mention} Has Been Kicked For Reason:", description=f"{reason}")
        msg=await ctx.channel.send(embed=emb)
        await member.kick(reason=reason)




def setup(client):
    client.add_cog(kick(client))