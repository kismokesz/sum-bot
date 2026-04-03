
import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Jegyek adatai (ide írd a tényleges számokat a jegyek alá)
jegyek = {
    "fidesz_berenc": [5, 3, 4],  # példa számok, cseréld le a valós adatokra
    "ellenzek": [2, 7, 1],        # példa másik szóra
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
        # Válasz a Discordra: számok listája + összeg
        await ctx.send(f"A 'fidesz_berenc' alatti számok: {szamok}\nÖsszegük: {osszeg}")
    else:
        await ctx.send("❌ Nincsenek számok ehhez a parancshoz!")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

# Token Railway environment variable-ból
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
