import datetime

import disnake
from disnake.ext import commands

class Settings:
    role_ids = [1274669048902193186, 1274668939519070259, 1274669011384143873]

class Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Выдаёт мут указанному  человеку на указанное время.")
    async def timeout(self, interaction, member: disnake.Member, time: int, reason: str):
        role_ids = Settings().role_ids
        role = disnake.utils.find(lambda r: r.id in role_ids, interaction.author.roles)

        if role:
            if member == interaction.author:
                return await interaction.response.send_message(
                    "Вы не можете замутить самого себя",
                    ephemeral=True
                )

            if time < 1:
                return await interaction.response.send_message(
                    "Вы не можете замутить пользователя на меньше 1 минуты",
                    ephemeral=True
                )

            time = datetime.datetime.now() + datetime.timedelta(minutes=time)
            await member.timeout(until=time, reason=reason)
            cool_time = disnake.utils.format_dt(time, style="R")
            embed = disnake.Embed(
                title="Таймаут",
                description=f"Пользователь {member.mention} был затайм-аутен. Причина: {reason}. "
                            f"Таймаут будет снят {cool_time}",
                color=0x2F3136
            ).set_thumbnail(url=member.display_avatar.url)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:

            embed2 = disnake.Embed(title="У вас  недостаточно прав", color=0xFFB02E)
            await interaction.response.send_message(embed=embed2, ephemeral=True)

    @commands.slash_command(description="Снимает мут с указанного человека.")
    async def un_timeout(self, interaction, member: disnake.Member):
        role_ids = Settings().role_ids
        role = disnake.utils.find(lambda r: r.id in role_ids, interaction.author.roles)

        if role:
             await member.timeout(until=None, reason=None)
             await interaction.response.send_message(
                 f"Таймаут с пользователя {member.mention} был снят",
                ephemeral=True
            )
        else:
            embed2 = disnake.Embed(title="У вас  недостаточно прав", color=0xFFB02E)
            await interaction.response.send_message(embed=embed2, ephemeral=True)

def setup(bot):
    bot.add_cog(Timeout(bot))