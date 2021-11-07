import discord
from discord.ext import commands

class ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("File: ban.py Loaded")


    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member,*,reason= "No Reason Provided"):
        emb=discord.Embed(title=f"User {member.mention} Has Been Banned For Reason:", description=f"{reason}")
        msg=await ctx.channel.send(embed=emb)
        await member.ban(reason=reason)




def setup(client):
    client.add_cog(ban(client))