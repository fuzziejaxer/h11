import discord
from discord.ext import commands

class mute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("File: mute.py Loaded")


    @commands.command(description="Mutes the specified user.")
    @commands.has_permissions(manage_messages=True)
    async def mute(self ,ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

        await member.add_roles(mutedRole, reason=reason)
        emb=discord.Embed(title=f"User {member.mention} Has Been Muted For Reason:", description=f"{reason}")
        msg=await ctx.channel.send(embed=emb)




    @commands.command(description="Unmutes a specified user.")
    @commands.has_permissions(manage_messages=True)
    async def unmute(self ,ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        embed=discord.Embed(title=f"User {member.mention} Has Been Un-Muted")
        msg=await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(mute(client))