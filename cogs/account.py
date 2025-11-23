import discord
from discord.ext import commands
import datetime

class Account(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, *, user: discord.Member = None):
        await ctx.message.delete()
        if user is None:
            user = ctx.author

        embed = discord.Embed(title=f"{user.name}'s Avatar", color=user.color)
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def banner(self, ctx, *, user: discord.Member = None):
        await ctx.message.delete()
        if user is None:
            user = ctx.author

        req = await self.bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
        banner_id = req["banner"]

        if banner_id:
            banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
            embed = discord.Embed(title=f"{user.name}'s Banner", color=user.color)
            embed.set_image(url=banner_url)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{user.name} does not have a banner.", delete_after=5)

    @commands.command(aliases=['ui'])
    async def userinfo(self, ctx, *, user: discord.Member = None):
        await ctx.message.delete()
        if user is None:
            user = ctx.author

        embed = discord.Embed(title=f"User Info - {user.name}", color=user.color)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="ID", value=user.id, inline=False)
        embed.add_field(name="Created At", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Joined At", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Roles", value=" ".join([role.mention for role in user.roles]), inline=False)
        embed.add_field(name="Top Role", value=user.top_role.mention, inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Account(bot))
