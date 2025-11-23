import discord
from discord.ext import commands
import random
import string

class DiscordUtils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['uicon'])
    async def usericon(self, ctx, user: discord.User = None):
        await ctx.message.delete()

        if not user:
            await ctx.send(f'> **[**ERROR**]**: Invalid input\n> __Command__: `usericon <@user>`', delete_after=5)
            return

        avatar_url = user.avatar.url if user.avatar else user.default_avatar.url

        await ctx.send(f"> {user.mention}'s avatar:\n{avatar_url}")

    @commands.command(aliases=['ginfo'])
    async def guildinfo(self, ctx):
        await ctx.message.delete()

        if not ctx.guild:
            await ctx.send("> **[**ERROR**]**: This command can only be used in a server", delete_after=5)
            return

        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(title=f"Guild Info - {ctx.guild.name}", color=discord.Color.blue())
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="ID", value=ctx.guild.id, inline=False)
        embed.add_field(name="Owner", value=ctx.guild.owner, inline=False)
        embed.add_field(name="Created At", value=ctx.guild.created_at.strftime(date_format), inline=False)
        embed.add_field(name="Members", value=ctx.guild.member_count, inline=False)
        embed.add_field(name="Channels", value=f"Text: {len(ctx.guild.text_channels)}\nVoice: {len(ctx.guild.voice_channels)}", inline=False)
        embed.add_field(name="Roles", value=len(ctx.guild.roles), inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=['gicon'])
    async def guildicon(self, ctx):
        await ctx.message.delete()

        if not ctx.guild:
            await ctx.send("> **[**ERROR**]**: This command can only be used in a server", delete_after=5)
            return

        await ctx.send(f"> **{ctx.guild.name} icon :**\n{ctx.guild.icon.url if ctx.guild.icon else '*NO ICON*'}")

    @commands.command(aliases=['gbanner'])
    async def guildbanner(self, ctx):
        await ctx.message.delete()

        if not ctx.guild:
            await ctx.send("> **[**ERROR**]**: This command can only be used in a server", delete_after=5)
            return

        await ctx.send(f"> **{ctx.guild.name} banner :**\n{ctx.guild.banner.url if ctx.guild.banner else '*NO BANNER*'}")

    @commands.command()
    async def nitro(self, ctx):
        await ctx.message.delete()

        await ctx.send(f"https://discord.gift/{''.join(random.choices(string.ascii_letters + string.digits, k=16))}")

def setup(bot):
    bot.add_cog(DiscordUtils(bot))
