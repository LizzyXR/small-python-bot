import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        assert self.bot.user is not None
        #print(f"{bot.user.name} is ready\n--------")
        print(f"{self.__class__.__name__} loaded")
    
    @commands.command()
    async def ping(self, ctx):
        #await ctx.send(f"hello {ctx.author.mention} :)")
        ping_embed = discord.Embed(title="ping", description="latency in ms", color=discord.Color.red())
        ping_embed.add_field(name=f"{self.bot.user.name}'s latency in ms: ", value=f"{round(self.bot.latency*1000)}ms.", inline=False)
        ping_embed.set_footer(text=f"Requested by {ctx.author.name}.", icon_url=ctx.author.avatar)
        await ctx.reply(embed=ping_embed)

async def setup(bot):
    await bot.add_cog(Ping(bot))