import disnake
from disnake.ext import commands
from random import randint

class CoinFlip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Подбросить монетку.")
    async def coinflip(self, interaction):
        number = randint(0, 1)
        arr = ["🌕", "🌑"]
        await interaction.response.send_message(f"{arr[number]}")

def setup(bot):
    bot.add_cog(CoinFlip(bot))