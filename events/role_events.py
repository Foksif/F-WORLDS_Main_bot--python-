import disnake
from disnake.ext import commands

class RoleEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.role_ids = ['role_id_1', 'role_id_2', 'role_id_3']

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.roles != after.roles:
            added_roles = set(after.roles) - set(before.roles)
            removed_roles = set(before.roles) - set(after.roles)

            async for entry in after.guild.audit_logs(limit=1, action=disnake.AuditLogAction.member_role_update):
                user_id = entry.user.id

            log_channel = self.bot.get_channel(1276627513724113047)  # Замените channel_id на ID канала, куда нужно отправлять логи
            log_message = f"\n\nРоли участника {after.mention} изменены:\n"

            if added_roles:
                log_message += f"Добавлены роли: {', '.join(role.mention for role in added_roles)}\n"

            if removed_roles:
                log_message += f"Удалены роли: {', '.join(role.mention for role in removed_roles)}\n"

            if user_id:
                user = after.guild.get_member(user_id)
                log_message += f"Изменено пользователем: {user.mention}"

            else:
                log_message += "Изменено неизвестным пользователем"
            await log_channel.send(log_message)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role_id = 1274672532728844289
        role = member.guild.get_role(role_id)

        if role:
            await member.add_roles(role)
            print(f"Assigned role with ID '{role_id}' to {member.name}")
        else:
            print(f"Role with ID '{role_id}' not found in the server")