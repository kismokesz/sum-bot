import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

bot.run(os.getenv("DISCORD_TOKEN")
