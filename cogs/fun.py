import discord
from discord.ext import commands
import random
import asyncio
import pyfiglet

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['911'])
    async def airplane(self, ctx):
        await ctx.message.delete()

        frames = [
            f''':man_wearing_turban::airplane:\t\t\t\t:office:''',
            f''':man_wearing_turban:\t:airplane:\t\t\t:office:''',
            f''':man_wearing_turban:\t\t::airplane:\t\t:office:''',
            f''':man_wearing_turban:\t\t\t:airplane:\t:office:''',
            f''':man_wearing_turban:\t\t\t\t:airplane::office:''',
            ''':boom::boom::boom:''']

        sent_message = await ctx.send(frames[0])

        for frame in frames[1:]:
            await asyncio.sleep(0.5)
            await sent_message.edit(content=frame)

    @commands.command(aliases=['mine'])
    async def minesweeper(self, ctx, size: int=5):
        await ctx.message.delete()

        size = max(min(size, 8), 2)
        bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for _ in range(size - 1)]
        is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
        has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
        m_numbers = [":one:", ":two:", ":three:", ":four:", ":five:", ":six:"]
        m_offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        message_to_send = "**Click to play**:\n"

        for y in range(size):
            for x in range(size):
                tile = "||{}||".format(chr(11036))
                if has_bomb(x, y):
                    tile = "||{}||".format(chr(128163))
                else:
                    count = 0
                    for xmod, ymod in m_offsets:
                        if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                            count += 1
                    if count != 0:
                        tile = "||{}||".format(m_numbers[count - 1])
                message_to_send += tile
            message_to_send += "\n"

        await ctx.send(message_to_send)

    @commands.command(aliases=['leet'])
    async def leetspeak(self, ctx, *, content: str):
        await ctx.message.delete()

        if not content:
            await ctx.send("> **[ERROR]**: Invalid command.\n> __Command__: `leetspeak <message>`", delete_after=5)
            return

        content = content.replace('a', '4').replace('A', '4').replace('e', '3').replace('E', '3').replace('i', '1').replace('I', '1').replace('o', '0').replace('O', '0').replace('t', '7').replace('T', '7').replace('b', '8').replace('B', '8')
        await ctx.send(content)

    @commands.command()
    async def dick(self, ctx, user: str=None):
        await ctx.message.delete()

        if not user:
            user = ctx.author.display_name

        size = random.randint(1, 15)
        dong = "=" * size

        await ctx.send(f"> **{user}**'s Dick size\n8{dong}D")

    @commands.command()
    async def reverse(self, ctx, *, content: str=None):
        await ctx.message.delete()

        if not content:
            await ctx.send("> **[ERROR]**: Invalid command.\n> __Command__: `reverse <message>`", delete_after=5)
            return

        content = content[::-1]
        await ctx.send(content)

    @commands.command()
    async def ascii(self, ctx, *, message=None):
        await ctx.message.delete()

        if not message:
            await ctx.send(f"> **[**ERROR**]**: Invalid command.\n> __Command__: `ascii <message>`", delete_after=5)
            return

        try:
            ascii_art = pyfiglet.figlet_format(message)
            await ctx.send(f"```\n{ascii_art}\n```", delete_after=5)
        except Exception as e:
            await ctx.send(f"> **[ERROR]**: An error occurred while generating the ASCII art. `{e}`", delete_after=5)

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question):
        await ctx.message.delete()
        responses = [
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'Yes – definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
            'Signs point to yes.',
            'Reply hazy, try again.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don\'t count on it.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Very doubtful.'
        ]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command()
    async def gayrate(self, ctx, user: discord.Member = None):
        await ctx.message.delete()
        if user is None:
            user = ctx.author
        await ctx.send(f'{user.name} is {random.randint(0, 100)}% gay')

    @commands.command()
    async def simprate(self, ctx, user: discord.Member = None):
        await ctx.message.delete()
        if user is None:
            user = ctx.author
        await ctx.send(f'{user.name} is {random.randint(0, 100)}% a simp')

    @commands.command()
    async def slots(self, ctx):
        await ctx.message.delete()
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)
        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
        if (a == b == c):
            await ctx.send(f"{slotmachine} All matching, you won! 🎉")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
        else:
            await ctx.send(f"{slotmachine} No match, you lost 😢")

def setup(bot):
    bot.add_cog(Fun(bot))
