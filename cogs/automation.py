import discord
from discord.ext import commands
import asyncio
from utils.config import Config

class Automation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config()

    @commands.command()
    async def autobeefer(self, ctx, action: str=None, user: discord.User=None):
        await ctx.message.delete()

        autobeefer_config = self.config.get('autobeefer')

        if action not in ["ON", "OFF"]:
            await ctx.send(f"> **[**ERROR**]**: Invalid action. Use `ON` or `OFF`.\n> __Command__: `autobeefer ON|OFF <@user>`", delete_after=5)
            return

        if not user:
            await ctx.send(f"> **[**ERROR**]**: Please specify a user to beef with.\n> __Command__: `autobeefer ON|OFF <@user>`", delete_after=5)
            return

        if action == "ON":
            if user.id not in autobeefer_config['users']:
                autobeefer_config['users'].append(user.id)
                self.config.set('autobeefer', autobeefer_config)
                await ctx.send(f"> Now beefing with `{str(user)}`", delete_after=5)
            else:
                await ctx.send(f"> `{str(user)}` is already being beefed with.", delete_after=5)

        elif action == "OFF":
            if user.id in autobeefer_config['users']:
                autobeefer_config['users'].remove(user.id)
                self.config.set('autobeefer', autobeefer_config)
                await ctx.send(f"> Stopped beefing with `{str(user)}`", delete_after=5)
            else:
                await ctx.send(f"> `{str(user)}` was not being beefed with.", delete_after=5)

    @commands.command()
    async def spam(self, ctx, amount: int=1, *, message: str="https://discord.gg/PKR7nM9j9U"):
        await ctx.message.delete()

        try:
            if amount <= 0:
                await ctx.send("> **[**ERROR**]**: Amount must be greater than 0", delete_after=5)
                return
            for _ in range(amount):
                await ctx.send(message)
                await asyncio.sleep(0.5)
        except ValueError:
            await ctx.send(f'> **[**ERROR**]**: Invalid input\n> __Command__: `spam <amount> <message>`', delete_after=5)

def setup(bot):
    bot.add_cog(Automation(bot))
