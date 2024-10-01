import disnake
from disnake.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Отчищяет указанное количество сообщений в чате.")
    async def clear(self, interaction, amount: int):
        role_ids = [1274669048902193186, 1274668939519070259]
        for role_id in role_ids:
            role = disnake.utils.get(interaction.author.roles, id=role_id)
            if role:
                embed = disnake.Embed(title="Clear", description=f"Удалено {amount} сообщений.", color=0xFFB02E)
                await interaction.response.send_message(embed=embed, ephemeral=True)
                await interaction.channel.purge(limit=amount)
                return
        embed2 = disnake.Embed(title="У вас  недостаточно прав", color=0xFFB02E)
        await interaction.response.send_message(embed=embed2, ephemeral=True)

def setup(bot):
    bot.add_cog(Clear(bot))