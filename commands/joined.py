from discord.ext import commands
import discord

class Joined(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        assert self.bot.user is not None
        print(f"{self.__class__.__name__} loaded")

    @commands.command()
    async def joined(self, ctx, *, member: discord.Member):
        if member.joined_at is None:
            await ctx.send(f"{member} has no join date")
        else:
            await ctx.send(f"{member} joined  the server at {discord.utils.format_dt(member.joined_at)}")

    @joined.error
    async def joined_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("did you mean ``!joined @user``?")

async def setup(bot):
    await bot.add_cog(Joined(bot))