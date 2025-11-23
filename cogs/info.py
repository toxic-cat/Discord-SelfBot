import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        await ctx.message.delete()

        embed = discord.Embed(
            title="TRIXXCORD v2",
            description="Bot Information",
            color=discord.Color.purple()
        )

        embed.add_field(name="Creator's Discord", value="`r1tam`", inline=False)
        embed.add_field(name="Creator's Instagram", value="`not_your_ritam`", inline=False)
        embed.add_field(name="Bot Language", value="`Python (discord.py-self)`", inline=False)

        embed.set_footer(text="TrixxCord || Made with <3 By Ritam")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
