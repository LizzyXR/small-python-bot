from discord.ext import commands
from dotenv import load_dotenv
import discord
import os

load_dotenv()
space = os.getenv("space")

class Secret(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        assert self.bot.user is not None
        print(f"{self.__class__.__name__} loaded")

    @commands.command()
    @commands.has_role(space)
    async def secret(self, ctx):
        await ctx.reply("welcome to Space")

    @secret.error
    async def secret_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("you do not have permission to do that.")


async def setup(bot):
    await bot.add_cog(Secret(bot))