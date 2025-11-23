import discord
from discord.ext import commands
import time
import requests
import datetime
import io
import qrcode
import string
import random
from gtts import gTTS

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.datetime.now(datetime.timezone.utc)

    @commands.command()
    async def uptime(self, ctx):
        await ctx.message.delete()

        now = datetime.datetime.now(datetime.timezone.utc)
        delta = now - self.start_time
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        if days:
            time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
        else:
            time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."

        uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)

        await ctx.send(uptime_stamp)

    @commands.command()
    async def ping(self, ctx):
        await ctx.message.delete()

        before = time.monotonic()
        message_to_send = await ctx.send("Pinging...")

        await message_to_send.edit(content=f"`{int((time.monotonic() - before) * 1000)} ms`")

    @commands.command()
    async def geoip(self, ctx, ip: str=None):
        await ctx.message.delete()

        if not ip:
            await ctx.send("> **[ERROR]**: Invalid command.\n> __Command__: `geoip <ip>`", delete_after=5)
            return

        try:
            r = requests.get(f'http://ip-api.com/json/{ip}')
            geo = r.json()
            embed = f"""**GEOLOCATE IP**\n
            > :pushpin: `IP`\n*{geo['query']}*
            > :globe_with_meridians: `Country-Region`\n*{geo['country']} - {geo['regionName']}*
            > :department_store: `City`\n*{geo['city']} ({geo['zip']})*
            > :map: `Latitute-Longitude`\n*{geo['lat']} - {geo['lon']}*
            > :satellite: `ISP`\n*{geo['isp']}*
            > :robot: `Org`\n*{geo['org']}*
            > :alarm_clock: `Timezone`\n*{geo['timezone']}*
            > :electric_plug: `As`\n*{geo['as']}*"""
            await ctx.send(embed)
        except Exception as e:
            await ctx.send(f'> **[**ERROR**]**: Unable to geolocate ip\n> __Error__: `{str(e)}`', delete_after=5)

    @commands.command()
    async def tts(self, ctx, *, content: str=None):
        await ctx.message.delete()

        if not content:
            await ctx.send("> **[ERROR]**: Invalid command.\n> __Command__: `tts <message>`", delete_after=5)
            return

        content = content.strip()

        tts = gTTS(text=content, lang="en")

        f = io.BytesIO()
        tts.write_to_fp(f)
        f.seek(0)

        await ctx.send(file=discord.File(f, f"{content[:10]}.wav"))

    @commands.command(aliases=['qrcode'])
    async def qr(self, ctx, *, text: str="https://discord.gg/PKR7nM9j9U"):
        qr = qrcode.make(text)

        img_byte_arr = io.BytesIO()
        qr.save(img_byte_arr)
        img_byte_arr.seek(0)

        await ctx.send(file=discord.File(img_byte_arr, "qr_code.png"))

    @commands.command()
    async def pingweb(self, ctx, website_url: str=None):
        await ctx.message.delete()

        if not website_url:
            await ctx.send("> **[ERROR]**: Invalid command.\n> __Command__: `pingweb <url>`", delete_after=5)
            return

        try:
            r = requests.get(website_url).status_code
            if r == 404:
                await ctx.send(f'> Website **down** *({r})*')
            else:
                await ctx.send(f'> Website **operational** *({r})*')
        except Exception as e:
            await ctx.send(f'> **[**ERROR**]**: Unable to ping website\n> __Error__: `{str(e)}`', delete_after=5)

    @commands.command()
    async def gentoken(self, ctx, user: str=None):
        await ctx.message.delete()

        code = "ODA"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))

        if not user:
            await ctx.send(''.join(code))
        else:
            await ctx.send(f"> {user}'s token is: ||{''.join(code)}||")

    @commands.command()
    async def quickdelete(self, ctx, *, message: str=None):
        await ctx.message.delete()

        if not message:
            await ctx.send(f'> **[**ERROR**]**: Invalid input\n> __Command__: `quickdelete <message>`', delete_after=2)
            return

        await ctx.send(message, delete_after=2)

    @commands.command()
    async def firstmessage(self, ctx):
        await ctx.message.delete()

        try:
            async for message in ctx.channel.history(limit=1, oldest_first=True):
                link = f"https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{message.id}"
                await ctx.send(f"> Here is the link to the first message: {link}", delete_after=5)
                break
            else:
                await ctx.send("> **[ERROR]**: No messages found in this channel.", delete_after=5)

        except Exception as e:
            await ctx.send(f"> **[ERROR]**: An error occurred while fetching the first message. `{e}`", delete_after=5)

    @commands.command()
    async def google(self, ctx, *, query):
        await ctx.message.delete()
        await ctx.send(f'https://www.google.com/search?q={query.replace(" ", "+")}')

    @commands.command()
    async def urban(self, ctx, *, term):
        await ctx.message.delete()
        url = f"https://api.urbandictionary.com/v0/define?term={term}"
        response = requests.get(url).json()
        if len(response["list"]) == 0:
            return await ctx.send(f"No results found for **{term}**.")

        definition = response["list"][0]["definition"]
        example = response["list"][0]["example"]

        embed = discord.Embed(title=f"Urban Dictionary: {term}", color=discord.Color.blue())
        embed.add_field(name="Definition", value=definition, inline=False)
        embed.add_field(name="Example", value=example, inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Utility(bot))
