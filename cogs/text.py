from discord.ext import commands
import random

class Text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tiny(self, ctx, *, text: str):
        await ctx.message.delete()
        mapping = {
            'a': 'ᵃ', 'b': 'ᵇ', 'c': 'ᶜ', 'd': 'ᵈ', 'e': 'ᵉ', 'f': 'ᶠ', 'g': 'ᵍ', 'h': 'ʰ', 'i': 'ᶦ',
            'j': 'ʲ', 'k': 'ᵏ', 'l': 'ˡ', 'm': 'ᵐ', 'n': 'ⁿ', 'o': 'ᵒ', 'p': 'ᵖ', 'q': 'ᵠ', 'r': 'ʳ',
            's': 'ˢ', 't': 'ᵗ', 'u': 'ᵘ', 'v': 'ᵛ', 'w': 'ʷ', 'x': 'ˣ', 'y': 'ʸ', 'z': 'ᶻ',
            'A': 'ᴬ', 'B': 'ᴮ', 'C': 'ᶜ', 'D': 'ᴰ', 'E': 'ᴱ', 'F': 'ᶠ', 'G': 'ᴳ', 'H': 'ᴴ', 'I': 'ᴵ',
            'J': 'ᴶ', 'K': 'ᴷ', 'L': 'ᴸ', 'M': 'ᴹ', 'N': 'ᴺ', 'O': 'ᴼ', 'P': 'ᴾ', 'Q': 'ᵠ', 'R': 'ᴿ',
            'S': 'ˢ', 'T': 'ᵀ', 'U': 'ᵁ', 'V': 'ᵛ', 'W': 'ᵂ', 'X': 'ˣ', 'Y': 'ʸ', 'Z': 'ᶻ',
            '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '0': '⁰'
        }
        await ctx.send("".join([mapping.get(c, c) for c in text]))

    @commands.command()
    async def zalgo(self, ctx, *, text: str):
        await ctx.message.delete()
        zalgo_chars = [
            u'\u030d', u'\u030e', u'\u0304', u'\u0305', u'\u033f', u'\u0311', u'\u0306', u'\u0310',
            u'\u0352', u'\u0357', u'\u0351', u'\u0307', u'\u0308', u'\u030a', u'\u0342', u'\u0343',
            u'\u0344', u'\u034a', u'\u034b', u'\u034c', u'\u0303', u'\u0302', u'\u030c', u'\u0350',
            u'\u0300', u'\u0301', u'\u030b', u'\u030f', u'\u0312', u'\u0313', u'\u0314', u'\u033d',
            u'\u0309', u'\u0363', u'\u0364', u'\u0365', u'\u0366', u'\u0367', u'\u0368', u'\u0369',
            u'\u036a', u'\u036b', u'\u036c', u'\u036d', u'\u036e', u'\u036f', u'\u033e', u'\u035b',
            u'\u0346', u'\u031a', u'\u031e', u'\u031c', u'\u031d', u'\u0334', u'\u0335', u'\u0336',
            u'\u034f', u'\u035c', u'\u035d', u'\u035e', u'\u035f', u'\u0360', u'\u0361', u'\u0362',
            u'\u0338', u'\u0337', u'\u0362', u'\u0489', u'\u0488'
        ]
        result = []
        for char in text:
            result.append(char)
            for _ in range(random.randint(1, 5)):
                result.append(random.choice(zalgo_chars))
        await ctx.send("".join(result))

def setup(bot):
    bot.add_cog(Text(bot))
