from discord.ext import commands
import discord

class Reply(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        assert self.bot.user is not None
        print(f"{self.__class__.__name__} loaded")

    @commands.command()
    async def reply(self, ctx):
        await ctx.reply("i'm replying to you")

async def setup(bot):
    await bot.add_cog(Reply(bot))