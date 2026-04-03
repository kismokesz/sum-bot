import os
import discord
from discord.ext import commands
import re

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Ping parancs teszteléshez
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# Sum parancs: üzenetenként összeadja a számokat
@bot.command(name="sum")
async def sum_numbers(ctx, limit: int = 50):  # alapértelmezett 50 üzenet
    async for message in ctx.channel.history(limit=limit):
        numbers = re.findall(r'\d+', message.content)
        numbers = [int(n) for n in numbers]
        if numbers:
            osszeg = sum(numbers)
            # Számok + jelekkel: "5 + 4 + 6 = 15"
            numbers_str = " + ".join(map(str, numbers))
            await ctx.send(f"Üzenet: `{message.content}`\nSzámok összege: {numbers_str} = {osszeg}")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

# Token Railway environment variable-ból
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
