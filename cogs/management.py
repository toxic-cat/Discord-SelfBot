import discord
from discord.ext import commands
from utils.config import Config
import asyncio

class Management(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config()

    @commands.command(aliases=['prefix'])
    async def changeprefix(self, ctx, *, new_prefix: str=None):
        await ctx.message.delete()

        if not new_prefix:
            await ctx.send(f"> **[**ERROR**]**: Invalid command.\n> __Command__: `changeprefix <prefix>`", delete_after=5)
            return

        self.config.set('prefix', new_prefix)
        self.bot.command_prefix = new_prefix

        await ctx.send(f"> Prefix updated to `{new_prefix}`", delete_after=5)

    @commands.command(aliases=["logout"])
    async def shutdown(self, ctx):
        await ctx.message.delete()

        msg = await ctx.send("> Shutting down...")
        await asyncio.sleep(2)

        await msg.delete()
        await self.bot.close()

    @commands.command()
    async def afk(self, ctx, status: str, *, message: str=None):
        await ctx.message.delete()

        afk_config = self.config.get('afk')

        if status not in ["ON", "OFF"]:
            await ctx.send(f"> **[**ERROR**]**: Invalid action. Use `ON` or `OFF`.\n> __Command__: `afk ON|OFF <message>`", delete_after=5)
            return

        if status.upper() == "ON":
            if not afk_config["enabled"]:
                afk_config["enabled"] = True
                if message:
                    afk_config["message"] = message
                self.config.set('afk', afk_config)
                await ctx.send(f"> **AFK mode enabled.** Message: `{afk_config['message']}`", delete_after=5)
            else:
                await ctx.send("> **[**ERROR**]**: AFK mode is already enabled", delete_after=5)
        elif status.upper() == "OFF":
            if afk_config["enabled"]:
                afk_config["enabled"] = False
                self.config.set('afk', afk_config)
                await ctx.send("> **AFK mode disabled.** Welcome back!", delete_after=5)
            else:
                await ctx.send("> **[**ERROR**]**: AFK mode is not currently enabled", delete_after=5)

    @commands.command(aliases=['autor'])
    async def autoreply(self, ctx, command: str, user: discord.User=None):
        await ctx.message.delete()

        autoreply_config = self.config.get('autoreply')

        if command not in ["ON", "OFF"]:
            await ctx.send(f"> **[**ERROR**]**: Invalid input. Use `ON` or `OFF`.\n> __Command__: `autoreply ON|OFF [@user]`", delete_after=5)
            return

        if command.upper() == "ON":
            if user:
                if user.id not in autoreply_config["users"]:
                    autoreply_config["users"].append(user.id)
                    self.config.set('autoreply', autoreply_config)
                await ctx.send(f"> **Autoreply enabled for user {user.mention}.**", delete_after=5)
            else:
                if ctx.channel.id not in autoreply_config["channels"]:
                    autoreply_config["channels"].append(ctx.channel.id)
                    self.config.set('autoreply', autoreply_config)
                await ctx.send("> **Autoreply has been enabled in this channel**", delete_after=5)
        elif command.upper() == "OFF":
            if user:
                if user.id in autoreply_config["users"]:
                    autoreply_config["users"].remove(user.id)
                    self.config.set('autoreply', autoreply_config)
                await ctx.send(f"> **Autoreply disabled for user {user.mention}**", delete_after=5)
            else:
                if ctx.channel.id in autoreply_config["channels"]:
                    autoreply_config["channels"].remove(ctx.channel.id)
                    self.config.set('autoreply', autoreply_config)
                await ctx.send("> **Autoreply has been disabled in this channel**", delete_after=5)

    @commands.command(aliases=["copycatuser", "copyuser"])
    async def copycat(self, ctx, action: str=None, user: discord.User=None):
        await ctx.message.delete()

        copycat_config = self.config.get('copycat')

        if action not in ["ON", "OFF"]:
            await ctx.send(f"> **[**ERROR**]**: Invalid action. Use `ON` or `OFF`.\n> __Command__: `copycat ON|OFF <@user>`", delete_after=5)
            return

        if not user:
            await ctx.send(f"> **[**ERROR**]**: Please specify a user to copy.\n> __Command__: `copycat ON|OFF <@user>`", delete_after=5)
            return

        if action == "ON":
            if user.id not in copycat_config['users']:
                copycat_config['users'].append(user.id)
                self.config.set('copycat', copycat_config)
                await ctx.send(f"> Now copying `{str(user)}`", delete_after=5)
            else:
                await ctx.send(f"> `{str(user)}` is already being copied.", delete_after=5)

        elif action == "OFF":
            if user.id in copycat_config['users']:
                copycat_config['users'].remove(user.id)
                self.config.set('copycat', copycat_config)
                await ctx.send(f"> Stopped copying `{str(user)}`", delete_after=5)
            else:
                await ctx.send(f"> `{str(user)}` was not being copied.", delete_after=5)

    @commands.command(aliases=['remote'])
    async def remoteuser(self, ctx, action: str, user: discord.User=None):
        await ctx.message.delete()

        if not user:
            await ctx.send("> **[ERROR]**: Invalid command.\n> __Command__: `remoteuser ADD|REMOVE <@user>`", delete_after=5)
            return

        if action not in ["ADD", "REMOVE"]:
            await ctx.send(f"> **[**ERROR**]**: Invalid action. Use `ADD` or `REMOVE`.\n> __Command__: `remoteuser ADD|REMOVE <@user>`", delete_after=5)
            return

        remote_users = self.config.get('remote_users')

        if action.upper() == "ADD":
            if user.id not in remote_users:
                remote_users.append(user.id)
                self.config.set('remote_users', remote_users)
                await ctx.send(f"> **Success**: {user.name} added to remote-users", delete_after=5)
            else:
                await ctx.send(f"> **[**ERROR**]**: {user.name} is already in remote-users", delete_after=5)
        elif action.upper() == "REMOVE":
            if user.id in remote_users:
                remote_users.remove(user.id)
                self.config.set('remote_users', remote_users)
                await ctx.send(f"> **Success**: {user.name} removed from remote-users", delete_after=5)
            else:
                await ctx.send(f"> **[**ERROR**]**: {user.name} is not in remote-users", delete_after=5)

def setup(bot):
    bot.add_cog(Management(bot))
