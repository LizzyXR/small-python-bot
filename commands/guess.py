from discord.ext import commands
import discord
import asyncio
import random

class Guess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        assert self.bot.user is not None
        print(f"{self.__class__.__name__} loaded")
    
    @commands.command()
    async def guess(self, ctx):
        await ctx.send("guess a number between 1 and 10, you have 5 seconds!")

        def is_correct(m):
            #return m.author == ctx.author and 1 <= int(m.content) <= 10 and m.content.isdigit()
            return(
                m.author == ctx.author
                and m.channel == ctx.channel
                and m.content.isdigit()
                and 1 <= int(m.content) <= 10
            )
        
        answer = random.randint(1,10)

        try:
            msg = await self.bot.wait_for("message", check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await ctx.reply(f"you took too long :(\nthe answer was {answer}")

        if int(msg.content) == answer:
            await ctx.reply(f"you guessed it! the answer was {answer}")
        else:
            await ctx.reply(f"wrong :(\nthe answer was {answer}")

async def setup(bot):
    await bot.add_cog(Guess(bot))