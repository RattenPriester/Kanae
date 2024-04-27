import glob
import os
import typing
import discord
import asyncio

from discord import app_commands
from discord.ext import commands



class psound(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#TODO fix error (ExtensionFailed: Extension 'cogs.sound' raised an error: TypeError: 'function' object is not subscriptable)
    async def psound_autocompletion(self, interaction: discord.Interaction, current: str) -> typing.List[app_commands.Choice[str]]:
        data=[]
        for v in os.listdir("sounds/*"):
            if v.endswith(".mp3") or v.endswith(".ogg"):
                sstr= v.split(".")
                
                data.append(app_commands.Choice(sstr))
                
        return data

    @app_commands.command(name="psound", description="plays a sound that you can select")
    @app_commands.describe(sound='the sound you want to play')
    @app_commands.autocomplete(sound=psound_autocompletion)
    async def psound(self, interaction: discord.interactions.Interaction, sound: str):
        voice_channel = interaction.user.voice.channel

        if voice_channel == None:
            await interaction.invoke(self._join)

        voice_client = await voice_channel.connect()
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(sound))
        voice_client.play(source)
        await interaction.response.send_message(f"playing {sound}")
        while voice_client.is_playing():
            await asyncio.sleep(1)
        await voice_client.disconnect()




async def setup(bot):
    await bot.add_cog(psound(bot))
