import discord
from discord.ext import commands
import json
import os
import platform
from colorama import Fore
import random
import itertools

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX

__version__ = "3.2"

with open("config.json", "r") as file:
    config = json.load(file)
    token = config.get("token")
    prefix = config.get("prefix")
    if config["autoreply"]["messages"]:
        message_generator = itertools.cycle(config["autoreply"]["messages"])

bot = commands.Bot(command_prefix=prefix, self_bot=True, help_command=None)

@bot.event
async def on_ready():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

    print(f"""\n{Fore.RESET}
                            ██████╗ ████████╗██╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗     
                           ██╔═══██╗╚══██╔══╝██║██╔═══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
                           ██║██╗██║   ██║   ██║██║   ██║       ██║   ██║   ██║██║   ██║██║     
                           ██║██║██║   ██║   ██║██║   ██║       ██║   ██║   ██║██║   ██║██║     
                           ╚█║████╔╝   ██║   ██║╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
                            ╚╝╚═══╝    ╚═╝   ╚═╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝\n""".replace('█', f'{b}█{y}'))
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------
{w}raadev {b}|{w} https://github.com/AstraaDev {b}|{w} https://github.com/AstraaDev {b}|{w} https://github.com/AstraaDev {b}|{w} https://github.com
{y}------------------------------------------------------------------------------------------------------------------------\n""")
    print(f"{y}[{b}+{y}]{w} SelfBot Information:\n")
    print(f"\t{y}[{w}#{y}]{w} Version: v{__version__}")
    print(f"\t{y}[{w}#{y}]{w} Logged in as: {bot.user} ({bot.user.id})")
    print(f"\t{y}[{w}#{y}]{w} Cached Users: {len(bot.users)}")
    print(f"\t{y}[{w}#{y}]{w} Guilds Connected: {len(bot.guilds)}\n\n")
    print(f"{y}[{b}+{y}]{w} Settings Overview:\n")
    print(f"\t{y}[{w}#{y}]{w} SelfBot Prefix: {prefix}")
    print(f"\t{y}[{w}#{y}]{w} Remote Users Configured: {len(config['remote_users'])}")
    print(f"\t{y}[{w}#{y}]{w} AFK Status: {'Enabled' if config['afk']['enabled'] else 'Disabled'}")
    print(f"\n{y}[{Fore.GREEN}!{y}]{w} SelfBot is now online and ready!")

@bot.event
async def on_message(message):
    if message.author.id in config["copycat"]["users"]:
        if message.content.startswith(config['prefix']):
            response_message = message.content[len(config['prefix']):]
            await message.reply(response_message)
        else:
            await message.reply(message.content)

    if config["autobeefer"]["enabled"] and message.author.id in config["autobeefer"]["users"]:
        await message.reply(random.choice(config["autobeefer"]["messages"]))

    if config["afk"]["enabled"]:
        if bot.user in message.mentions and message.author != bot.user:
            await message.reply(config["afk"]["message"])
            return
        elif isinstance(message.channel, discord.DMChannel) and message.author != bot.user:
            await message.reply(config["afk"]["message"])
            return

    if message.author != bot.user:
        if str(message.author.id) in config["autoreply"]["users"]:
            autoreply_message = next(message_generator)
            await message.reply(autoreply_message)
            return
        elif str(message.channel.id) in config["autoreply"]["channels"]:
            autoreply_message = next(message_generator)
            await message.reply(autoreply_message)
            return
    
    if message.guild and message.guild.id == 1279905004181917808 and message.content.startswith(config['prefix']):
        await message.delete()
        await message.channel.send("> SelfBot commands are not allowed here. Thanks.", delete_after=5)
        return

    if message.author != bot.user and str(message.author.id) not in config["remote_users"]:
        return

    await bot.process_commands(message)

if __name__ == "__main__":
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token)
