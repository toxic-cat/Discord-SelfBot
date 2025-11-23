import discord
from discord.ext import commands
import asyncio

class Cloning(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clone(self, ctx):
        await ctx.message.delete()
        guild = ctx.guild
        new_guild = await self.bot.create_guild(name=f"Copy of {guild.name}")

        for c in await guild.fetch_channels():
            if isinstance(c, discord.TextChannel):
                overwrites = {
                    new_guild.default_role: c.overwrites_for(guild.default_role),
                    new_guild.me: c.overwrites_for(guild.me)
                }
                new_channel = await new_guild.create_text_channel(name=c.name, category=c.category, topic=c.topic, overwrites=overwrites)
            elif isinstance(c, discord.VoiceChannel):
                overwrites = {
                    new_guild.default_role: c.overwrites_for(guild.default_role),
                    new_guild.me: c.overwrites_for(guild.me)
                }
                new_channel = await new_guild.create_voice_channel(name=c.name, category=c.category, overwrites=overwrites)

        for role in guild.roles:
            if role.name != "@everyone":
                await new_guild.create_role(name=role.name, permissions=role.permissions, colour=role.colour, hoist=role.hoist, mentionable=role.mentionable)

        await asyncio.sleep(3)

        info = await new_guild.text_channels[0].create_invite(reason="Cloned server")

        await ctx.author.send(f"Cloned server {guild.name}, new server invite: {info.url}")

def setup(bot):
    bot.add_cog(Cloning(bot))
