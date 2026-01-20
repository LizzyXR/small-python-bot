from discord.ext import commands
import discord

class slapperConverter(commands.Converter):
    async def convert(self, ctx, argument):
        parts = argument.split(" ", 1)

        if len(parts) < 2:
            raise commands.BadArgument("specify a reason to slap someone, and also mention them you doofus")

        member_str, reason = parts
        member = await commands.MemberConverter().convert(ctx, member_str)
        return f"{ctx.author.mention} slapped {member.mention} because ***{reason}***"

class Slap(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        assert self.bot.user is not None
        print(f"{self.__class__.__name__} loaded")

    @commands.command()
    async def slap(self, ctx, *, reason: slapperConverter):
        await ctx.send(reason)

    @slap.error
    async def slap_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("you must at least specify a reason to slap someone..")
        elif isinstance(error, commands.BadArgument):
            await ctx.reply(f"uhmm..\n{str(error)}")
    
async def setup(bot):
    await bot.add_cog(Slap(bot))