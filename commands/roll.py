from discord.ext import commands
import random
import discord

class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        assert self.bot.user is not None
        print(f"{self.__class__.__name__} loaded")

    @commands.command()
    async def roll(self, ctx, dice: str):
        try:
            rolls, limit = map(int, dice.split("d"))
        except Exception:
            await ctx.reply("format has to be in NdN")
            return
        
        result = ", ".join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.reply(result)

    @roll.error
    async def roll_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("it needs parameters, format has to be NdN\nfor example, to roll a dice with 6 sides and 1 try: ``!roll 1d6``")

async def setup(bot):
    await bot.add_cog(Roll(bot))