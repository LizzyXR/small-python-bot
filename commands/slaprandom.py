from discord.ext import commands
import discord
import random

class randomSlapperConverter(commands.Converter):
    async def convert(self, ctx, argument):
        members = [m for m in ctx.guild.members if not m.bot]

        if not members:
            raise commands.BadArgument("something went wrong and i couldn't slap anyone for you :(")
        
        to_slap = random.choice(members)
        
        return f"{ctx.author.mention} slapped {to_slap.mention} because ***{argument}***"

class slapRandom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        assert self.bot.user is not None
        print(f"{self.__class__.__name__} loaded")

    @commands.command()
    async def slaprandom(self, ctx, *, reason: randomSlapperConverter):
        await ctx.send(reason)

    @slaprandom.error
    async def slaprandom_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("you must at least specify a reason to slap someone..")
        elif isinstance(error, commands.BadArgument):
            await ctx.reply(f"uhmm..\n{str(error)}")

async def setup(bot):
    await bot.add_cog(slapRandom(bot))