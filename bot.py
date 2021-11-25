import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix="=", case_insensitive=True)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Listening For Commands."))
    print(f"{client.user.name} is ready.")
    
@client.command()
async def vote(ctx):
    ctx.send("Vote For H11 Here: \n https://top.gg/bot/906611513052250172/vote")

@client.command()
@commands.has_permissions(administrator=True)
async def setprefix(ctx, prefix):
    client.command_prefix = prefix
    await ctx.send(f"Prefix changed to ``{prefix}``")

@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("")
