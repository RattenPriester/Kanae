import glob
import discord
import asyncio

from discord import app_commands
from discord.ext import commands



class sound(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="psound", description="plays a sound that you can select")
    @app_commands.choices(sounds=[])
    @app_commands.describe(sound='the sound you want to play')
    async def psound(self, ctx: discord.interactions.Interaction, sound: str):
        voice_channel = ctx.user.voice.channel
        voice_client = await voice_channel.connect()
        sounds = glob.glob("\sounds*.mp3")
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(sounds))
        voice_client.play(source)
        while voice_client.is_playing():
            await asyncio.sleep(1)
        await voice_client.disconnect()
        

async def setup(bot):
    await bot.add_cog(sound(bot))
