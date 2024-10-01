import disnake
from disnake.ext import commands



class Settings:
#     Roles
    AdminID = 1274669048902193186
    ModerID = 1274668939519070259
    HelperID = 1274669011384143873

    Male = 1274673154618556470
    Female = 1274672743068991530


class ButtonView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Minecraft (Development)", style=disnake.ButtonStyle.gray, custom_id="button1")
    async def button1(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        await interaction.response.send_message("Ошибка получения данных  с удалённого сервера! (Функция находится в разработке)\nLine: 231 (Stats.java)", ephemeral=True)

    @disnake.ui.button(label="Discord", style=disnake.ButtonStyle.primary, custom_id="button2")
    async def button2(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        guild = interaction.guild
        member_count = guild.member_count

        def count(role_id):
            role = guild.get_role(role_id)
            role_count = len(role.members)
            return role_count

        staff = count(Settings().AdminID) + count(Settings().ModerID) + count(Settings().HelperID)

        embed = disnake.Embed(color=0xFFB02E)
        embed.description = f"> **Участников в discord:** {member_count} \n" \
        f"> **Парней:** {count(Settings().Male)} \n"\
        f"> **Девушек:** {count(Settings().Female)} \n" \
        f"> **Персонал:** {staff}"
        await interaction.response.send_message(embed=embed, ephemeral=True)


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Показывает статистику Discord или Minecraft сервера.")
    async def stats(self, interaction):
        view = ButtonView()

        embed = disnake.Embed( colour=0xFFB02E)
        embed.set_image(url="https://share.creavite.co/66c8a701ce0e5d041d7b55a5.gif")
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

def setup(bot):
    bot.add_cog(Stats(bot))