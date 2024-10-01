import disnake
from disnake.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Показывает аватарку выбранного пользователя.")
    async def avatar(self, interaction, member: disnake.Member = None):
        user = member or interaction.author
        embed = disnake.Embed(title=f"Avatar {user.display_name}", color=0x00ff00)
        embed.set_image(url=user.display_avatar.url)
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Avatar(bot))