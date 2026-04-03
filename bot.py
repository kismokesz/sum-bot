import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()  # Lokálisan kell, Railway-n a környezeti változók automatikusak

TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"{bot.user} elindult!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(TOKEN)
