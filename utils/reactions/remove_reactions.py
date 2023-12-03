import discord


async def remove_reaction(payload, bot):
    self_roles_1_id = 1027668015791214673
    self_roles_cyber_team_id = 1031750672141537352
    self_roles_helper_id = 1031755073128247397
    # self_roles_verify_id = 1059559943071608853
    if self_roles_1_id == payload.message_id:
        guild = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name
        if emoji == 'Student':
            role = discord.utils.get(guild.roles, name='Student')
        elif emoji == 'SystemAdministrator':
            role = discord.utils.get(guild.roles, name='System Administrator')
        elif emoji == 'MalwareAnalyst':
            role = discord.utils.get(guild.roles, name='Malware Analyst')
        elif emoji == 'PenetrationTester':
            role = discord.utils.get(guild.roles, name='Penetration Tester')
        elif emoji == 'BugHunter':
            role = discord.utils.get(guild.roles, name='Bug Hunter')
        elif emoji == 'CTFPlayer':
            role = discord.utils.get(guild.roles, name='CTF Player')
        elif emoji == 'OpenSourceContributor':
            role = discord.utils.get(guild.roles, name='Opensource Contributor')
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)
            print(f"Remove: {role}.")
        else:
            print("Member not found")

    # RedTeam roles
    cyber_teams_message_id = self_roles_cyber_team_id
    if cyber_teams_message_id == payload.message_id:
        guild = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name
        if emoji == 'BlueTeam':
            role = discord.utils.get(guild.roles, name='Blue Team')
        elif emoji == 'RedTeam':
            role = discord.utils.get(guild.roles, name='Red Team')
        elif emoji == 'PurpleTeam':
            role = discord.utils.get(guild.roles, name='Purple Team')
        member = await(guild.fetch_member(payload.user_id))

        if member is not None:
            await member.remove_roles(role)
            print(f"Remove: {role}.")
        else:
            print("Member not found")

    # Helper role
    helper_message_id = self_roles_helper_id
    if helper_message_id == payload.message_id:
        guild = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name
        if emoji == 'Helper':
            role = discord.utils.get(guild.roles, name='Helper')
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)
            print(f"Remove: {role}.")
        else:
            print("Member not found")
