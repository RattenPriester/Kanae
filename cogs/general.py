import discord

from discord import app_commands
from discord.ext import commands



class general(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    
    @app_commands.command(name="avatar", description="Sends user's avatar in a embed (sends own avatar if user is left none)")
    async def avatar(self, interaction: discord.Interaction, member: discord.Member=None):
        if member is None:
            member= interaction.user
        elif member is not None:
            member=member

        avatar_embed = discord.Embed(title=f"{member.name}'s Avatar", color=0xff0000)
        avatar_embed.set_image(url=member.avatar)
        avatar_embed.set_footer(text=f"Requested by {member.name}",icon_url=member.avatar )

        await interaction.response.send_message(embed=avatar_embed)


async def setup(bot):
    await bot.add_cog(general(bot))