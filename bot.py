import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Jegyek adatai
jegyek = {
    "fidesz_berenc": [5, 3, 4],  # ide írd a tényleges számokat
    "ellenzek": [2, 7, 1],        # példa más szóra
}

# Ping parancs teszteléshez
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# Fidesz Berenc parancs
@bot.command(name="fidesz_berenc")
async def fidesz_berenc(ctx):
    szamok = jegyek.get("fidesz_berenc", [])
    if szamok:
        osszeg = sum(szamok)
        await ctx.send(f"A 'fidesz_berenc' alatti számok összege: {osszeg}")
    else:
        await ctx.send("❌ Nincsenek számok ehhez a parancshoz!")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

# Token Railway environment variable-ból
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
