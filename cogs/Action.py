import disnake
from disnake.ext import commands

class Settings:
    role_ids = [1274669340821684224, 1275563458397474928]
    consoleId = 1276874963189497877

    player = 1274789247072731227
    free_player = 1278224000551485440

class ButtonView(disnake.ui.View):
    def __init__(self, player, user):
        super().__init__(timeout=None)
        self.player_name = player
        self.user = user

        self.console = Settings().consoleId

        self.player = Settings().player
        self.free_player = Settings().free_player


    @disnake.ui.button(label="Выдать бесплатную проходку", style=disnake.ButtonStyle.green, custom_id="button1")
    async def button1(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        role_ids = Settings().role_ids
        role = disnake.utils.find(lambda r: r.id in role_ids, interaction.author.roles)

        if role:
            channel = interaction.guild.get_channel(self.console)
            player = interaction.guild.get_role(self.player)
            free_player = interaction.guild.get_role(self.free_player)

            if channel is None:
                await interaction.response.send_message("Канал не найден.", ephemeral=True)
                return

            message = f"easywl add {self.player_name}"

            await self.user.add_roles(player)
            await self.user.add_roles(free_player)
            await channel.send(message)
            await interaction.response.send_message(f"Бесплатная проходка для игрока {self.user.mention} была успешно выдана!", ephemeral=True)
        else:
            embed2 = disnake.Embed(title="У вас  недостаточно прав", color=0xFFB02E)
            await interaction.response.send_message(embed=embed2, ephemeral=True)

    @disnake.ui.button(label="Выдать платную проходку", style=disnake.ButtonStyle.green, custom_id="button2")
    async def button2(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        role_ids = Settings().role_ids
        role = disnake.utils.find(lambda r: r.id in role_ids, interaction.author.roles)

        if role:
            channel = interaction.guild.get_channel(self.console)
            player = interaction.guild.get_role(self.player)

            if channel is None:
                await interaction.response.send_message("Канал не найден.", ephemeral=True)
                return

            message = f"easywl add {self.player_name}"

            await self.user.add_roles(player)
            await channel.send(message)

            await interaction.response.send_message(f"Платная проходка для игрока {self.user.mention} была успешно выдана!", ephemeral=True)
        else:
            embed2 = disnake.Embed(title="У вас  недостаточно прав", color=0xFFB02E)
            await interaction.response.send_message(embed=embed2, ephemeral=True)

    @disnake.ui.button(label="Забрать проходку", style=disnake.ButtonStyle.danger, custom_id="button3")
    async def button3(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        role_ids = Settings().role_ids
        role = disnake.utils.find(lambda r: r.id in role_ids, interaction.author.roles)

        if role:
            channel = interaction.guild.get_channel(self.console)

            player = interaction.guild.get_role(self.player)
            free_player = interaction.guild.get_role(self.free_player)

            await interaction.user.remove_roles(player)
            await interaction.user.remove_roles(free_player)

            message = f"easywl remove {self.player_name}"
            await channel.send(message)
            await interaction.response.send_message(f"Проходка у игрока {self.user.mention} была успешно отнята!", ephemeral=True)

        else:
            embed2 = disnake.Embed(title="У вас  недостаточно прав", color=0xFFB02E)
            await interaction.response.send_message(embed=embed2, ephemeral=True)

class Action(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Взаимодействие с игроком")
    async def action(self, interaction, player: str, user: disnake.Member):
        role_ids = Settings().role_ids
        role = disnake.utils.find(lambda r: r.id in role_ids, interaction.author.roles)
        view = ButtonView(player, user)

        if role:
            embed = disnake.Embed(title=f"Взаимодействие с игроком", description=f"Игровое имя: {player} \n Дискорд: {user.mention}", color=0xFFB02E)
            await interaction.response.send_message(embed=embed, ephemeral=True, view=view)
        else:
            embed2 = disnake.Embed(title="У вас  недостаточно прав", color=0xFFB02E)
            await interaction.response.send_message(embed=embed2, ephemeral=True)
def setup(bot):
    bot.add_cog(Action(bot))