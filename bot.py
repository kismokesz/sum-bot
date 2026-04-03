import os
import discord
from discord.ext import commands
import re

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

@bot.command(name="fidesz_berenc")
async def fidesz_berenc(ctx, limit: int = 50):
    """Összeszámolja az utolsó `limit` üzenetben található számokat és kiírja üzenetenként is."""
    total_sum = 0
    results = []
    
    async for message in ctx.channel.history(limit=limit):
        numbers = [int(n) for n in re.findall(r'\d+', message.content)]
        if numbers:
            message_sum = sum(numbers)
            total_sum += message_sum
            # Üzenetenkénti részlet
            results.append(f"Üzenet: '{message.content}' → számok: {numbers}, összege: {message_sum}")
    
    # Kiírjuk az üzenetenkénti összegeket
    if results:
        for line in reversed(results):  # fordítva, hogy a legfrissebb üzenet legyen legfelül
            await ctx.send(line)
        await ctx.send(f"**Teljes összeg az utolsó {limit} üzenetben:** {total_sum}")
    else:
        await ctx.send("❌ Nem találtam számokat az utolsó üzenetekben!")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
