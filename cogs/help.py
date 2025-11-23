import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')

    @commands.command(aliases=['h'])
    async def help(self, ctx, page: int = 1):
        await ctx.message.delete()

        pages = [
            {
                "title": "Fun Commands",
                "commands": [
                    {"name": "airplane", "description": "Sends a 9/11 attack (warning: use responsibly)."},
                    {"name": "minesweeper", "description": "Play a game of Minesweeper with custom grid size."},
                    {"name": "leetspeak", "description": "Speak like a hacker, replacing letters."},
                    {"name": "dick", "description": "Show the 'size' of a user's dick."},
                    {"name": "reverse", "description": "Reverse the letters of a message."},
                    {"name": "ascii", "description": "Convert a message to ASCII art."}
                ]
            },
            {
                "title": "Utility Commands",
                "commands": [
                    {"name": "uptime", "description": "Returns how long the selfbot has been running."},
                    {"name": "ping", "description": "Returns the bot's latency."},
                    {"name": "geoip", "description": "Looks up the IP's location."},
                    {"name": "tts", "description": "Converts text to speech and sends an audio file (.wav)."},
                    {"name": "qr", "description": "Generate a QR code from the provided text and send it as an image."},
                    {"name": "pingweb", "description": "Ping a website and return the HTTP status code (e.g., 200 if online)."},
                    {"name": "gentoken", "description": "Generate an invalid but correctly patterned token."},
                    {"name": "quickdelete", "description": "Send a message and delete it after 2 seconds."},
                    {"name": "firstmessage", "description": "Get the link to the first message in the current channel."}
                ]
            },
            {
                "title": "Discord Utils Commands",
                "commands": [
                    {"name": "usericon", "description": "Get the profile picture of a user."},
                    {"name": "guildinfo", "description": "Get information about the current server."},
                    {"name": "guildicon", "description": "Get the icon of the current server."},
                    {"name": "guildbanner", "description": "Get the banner of the current server."},
                    {"name": "nitro", "description": "Generate a fake Nitro code."}
                ]
            },
            {
                "title": "Management Commands",
                "commands": [
                    {"name": "changeprefix", "description": "Change the bot's prefix."},
                    {"name": "shutdown", "description": "Stop the selfbot."},
                    {"name": "afk", "description": "Enable or disable AFK mode."},
                    {"name": "autoreply", "description": "Enable or disable automatic replies."},
                    {"name": "copycat", "description": "Automatically reply with the same message whenever the mentioned user speaks."}
                ]
            }
        ]

        if 1 <= page <= len(pages):
            page_data = pages[page - 1]
            embed = discord.Embed(title=page_data["title"], color=discord.Color.blue())
            for command in page_data["commands"]:
                embed.add_field(name=f"`{self.bot.command_prefix}{command['name']}`", value=command['description'], inline=False)

            embed.set_footer(text=f"Page {page}/{len(pages)}")
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Invalid page number. Please choose a page between 1 and {len(pages)}.", delete_after=5)

def setup(bot):
    bot.add_cog(Help(bot))
