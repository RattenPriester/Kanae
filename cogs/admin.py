from typing import Optional

import discord

from discord import app_commands
from discord.ext import commands


class admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.has_permissions(send_messages=True)
    @app_commands.command(name="ban",
                          description="bans people that are not artig!")
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: Optional[str]):
        await member.ban(reason=reason)
        ban_embed = discord.Embed(title=f"banned {member.name}", color=0xff0000)
        ban_embed.add_field(name="Reason",value=f"{reason}")
        ban_embed.set_footer(text=f"Requested by {member.name}", icon_url=member.avatar)

        await interaction.response.send_message(embed=ban_embed)

async def setup(bot):
    await bot.add_cog(admin(bot))