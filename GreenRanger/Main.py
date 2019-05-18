import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("bot is ready niggaaaaaa!")

client.run('NTU0ODAwNzE0MjU0MjU0MDky.XOBk2A.bEJMOiPW7gYPREn7FU4_bBYnxac')
