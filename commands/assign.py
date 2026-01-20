from discord.ext import commands
from dotenv import load_dotenv
import discord
import os

load_dotenv()
space = os.getenv("space")

class Assign(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        assert self.bot.user is not None
        print(f"{self.__class__.__name__} loaded")

    @commands.command()
    async def assign(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name=space)
        if role:
            await ctx.author.add_roles(role)
            await ctx.send(f"{ctx.author.mention} is now assigned to {space}")
        else:
            await ctx.reply("the role doesn't exist")

async def setup(bot):
    await bot.add_cog(Assign(bot))