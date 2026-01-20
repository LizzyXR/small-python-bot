from discord.ext import commands
import datetime
import discord

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        assert self.bot.user is not None
        print(f"{self.__class__.__name__} loaded")

    @commands.command()
    async def poll(self, ctx, *, question):
        embed = discord.Embed(title="Poll", description=question, color=0x700505, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"Poll created by {ctx.message.author.name}", icon_url=ctx.author.avatar)

        poll_message = await ctx.send(embed=embed)

        await poll_message.add_reaction("👍")
        await poll_message.add_reaction("👎")

async def setup(bot):
    await bot.add_cog(Poll(bot))