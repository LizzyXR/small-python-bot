from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import discord
import logging
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
space = os.getenv("space")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, activity=discord.Game(name="Gay Furry Hentai Simulator"))

@bot.event
async def on_ready():
    assert bot.user is not None
    print(f"{bot.user.name} is ready, loading cogs.\n--------")

@bot.event
async def on_member_join(member):
    await member.send(f"welcome {member.name}!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!editme"):
        message = await message.channel.send("what's 9+10?")
        await asyncio.sleep(3.0)
        await message.edit(content="21")

    if "meow" in message.content.lower():
        await message.delete()
        await message.channel.send(f"no meowing, mr/ms {message.author.mention} :cat:")
    
    await bot.process_commands(message)

@bot.event
async def on_message_edit(self, before, after):
    message = f"**{before.author}** edited their message:\n{before.content} -> {after.content}"
    await before.channel.send(message)

# --------------------------------------------------------------------------------------- #

def setup_logging():
    handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
    logging.basicConfig(level=logging.DEBUG, handlers=[handler], format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")

async def load():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            await bot.load_extension(f"commands.{filename[:-3]}")

async def main():
    setup_logging()

    async with bot:
        await load()
        await bot.start(token=token) # env

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\nExited safely.")
