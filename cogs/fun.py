import discord
import aiohttp
import random2

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
                embed.set_image(url=res['data']['children'][random2.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    #@app_commands.command(name="bjoke", description="sends a German joke that is not funny")
    #async def bjoke(self, interaction: discord.Interaction):
    #    with open("data/utils/bjokes.json", 'r', encoding='utf-8') as file:
    #        data = json.load(file)
    #        bjokes = data['bjokes']
    #        random_bjokes = random.choice(bjokes)
        
    #    embed= discord.Embed(title="Bad Joke")
    #    embed.set_thumbnail(url="https://tenor.com/view/laughing-hilarious-lol-funny-gif-4835730214933498337")
    #    embed.add_field(name="Joke", value=random_bjokes, inline=False)

    #    await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(fun(bot))


    