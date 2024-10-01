import disnake
from disnake.ext import commands, tasks
from events import RoleEvents
import os

intents = disnake.Intents.all()

activities = [
    disnake.Activity(type=disnake.ActivityType.watching, name="By Foks_f"),
    disnake.Activity(type=disnake.ActivityType.watching, name="Version 1.1.4 [alfa]")
]

bot = commands.Bot(command_prefix="f!", intents=intents, test_guilds=[1157195772115292252])

bot.add_cog(RoleEvents(bot))

@bot.event
async def on_ready():
    change_status.start()
    print(f'{bot.user} is ready!')

for file in os.listdir("./cogs"):
  if file.endswith(".py"):
    bot.load_extension(f"cogs.{file[:-3]}")

@tasks.loop(seconds=30)
async def change_status():
    if bot.is_ready():
        activity = activities[change_status.current_loop % len(activities)]
        await bot.change_presence(status=disnake.Status.idle, activity=activity)


bot.run("")
