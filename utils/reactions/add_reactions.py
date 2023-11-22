import discord

async def add_reactions(our_message_id, payload, self_roles_cyber_team_id, self_roles_helper_id, self_roles_verify_id):
    if our_message_id == payload.message_id:
        member = payload.member
        guild = member.guild
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
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        await member.add_roles(role)

        # These roles can be given by the admins only
        # pro_message_id = self_roles_pro_id
        # if pro_message_id == payload.message_id:
        #     member = payload.member
        #     guild = member.guild
        #     emoji = payload.emoji.name
        #
        #     if emoji == 'Volunteer':
        #         role = discord.utils.get(guild.roles, name='Student')
        #     elif emoji == 'Professional':
        #         role = discord.utils.get(guild.roles, name='Professional')
        #     elif emoji == 'Volunteer':
        #         role = discord.utils.get(guild.roles, name='System Administrator')
        #     else:
        #         role = discord.utils.get(guild.roles, name=payload.emoji.name)
        #     await member.add_roles(role)

    # RedTeam roles
    cyber_teams_message_id = self_roles_cyber_team_id
    if cyber_teams_message_id == payload.message_id:
        member = payload.member
        guild = member.guild
        emoji = payload.emoji.name
        if emoji == 'BlueTeam':
            role = discord.utils.get(guild.roles, name='Blue Team')
        elif emoji == 'RedTeam':
            role = discord.utils.get(guild.roles, name='Red Team')
        elif emoji == 'PurpleTeam':
            role = discord.utils.get(guild.roles, name='Purple Team')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        await member.add_roles(role)

    # Helper roles
    helper_message_id = self_roles_helper_id
    if helper_message_id == payload.message_id:
        member = payload.member
        guild = member.guild
        emoji = payload.emoji.name
        if emoji == 'Helper':
            role = discord.utils.get(guild.roles, name='Helper')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        await member.add_roles(role)

    # Verify roles
    verify_message_id = self_roles_verify_id
    if verify_message_id == payload.message_id:
        member = payload.member
        guild = member.guild
        emoji = payload.emoji.name
        if emoji == 'Checkbox':
            role = discord.utils.get(guild.roles, name='verified')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        await member.add_roles(role)