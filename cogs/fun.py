import discord
import aiohttp
import random

from discord.ext import commands



class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='memes from r/memes')
    async def meme2(self, ctx):
        embed = discord.Embed(title="**MEME**", description="meme from r/memes")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(fun(bot))


    