from discord.ext import commands
import discord

class Dm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} loaded")

    @commands.command()
    async def dm(self, ctx, *, msg):
        await ctx.author.send(f"you said: {msg}")

async def setup(bot):
    await bot.add_cog(Dm(bot))