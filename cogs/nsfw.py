"""
This cog contains NSFW commands. By using these commands, you acknowledge that you are of legal age to view NSFW content.
"""

import discord
from discord.ext import commands
import aiohttp
import random

class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def get_nsfw_image(self, endpoint):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.life/api/v2/img/{endpoint}") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data.get("url")
        return None

    @commands.command()
    @commands.is_nsfw()
    async def lesbian(self, ctx):
        await ctx.message.delete()
        url = await self.get_nsfw_image("les")
        if url:
            embed = discord.Embed(title="Lesbian", color=discord.Color.purple())
            embed.set_image(url=url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Could not fetch image.", delete_after=5)

    @commands.command()
    @commands.is_nsfw()
    async def boobs(self, ctx):
        await ctx.message.delete()
        url = await self.get_nsfw_image("boobs")
        if url:
            embed = discord.Embed(title="Boobs", color=discord.Color.purple())
            embed.set_image(url=url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Could not fetch image.", delete_after=5)

    @commands.command()
    @commands.is_nsfw()
    async def pussy(self, ctx):
        await ctx.message.delete()
        url = await self.get_nsfw_image("pussy")
        if url:
            embed = discord.Embed(title="Pussy", color=discord.Color.purple())
            embed.set_image(url=url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Could not fetch image.", delete_after=5)

def setup(bot):
    bot.add_cog(NSFW(bot))
