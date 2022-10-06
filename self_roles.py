from discord.ext import commands
import discord


def self_roles():
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    bot = discord.Client(intents=intents)

    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_raw_reaction_add(payload):
        our_message_id = 1027600476335779950

        if our_message_id == payload.message_id:
            member = payload.member
            guild = member.guild

            emoji = payload.emoji.name

            if emoji == 'Student':
                role = discord.utils.get(guild.roles, name='Student')
                print("Role: Student.")

            elif emoji == 'BugHunter':
                role = discord.utils.get(guild.roles, name='Bug Hunter')
                print("Role: Bug Hunter.")

            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)
            await member.add_roles(role)

    @bot.event
    async def on_raw_reaction_remove(payload):
        our_message_id = 1027600476335779950

        if our_message_id == payload.message_id:
            guild = await(bot.fetch_guild(payload.guild_id))
            emoji = payload.emoji.name
            if emoji == 'Student':
                role = discord.utils.get(guild.roles, name='Student')
                print("Remove: Student.")

            elif emoji == 'BugHunter':
                role = discord.utils.get(guild.roles, name='Bug Hunter')
                print("Remove: Bug Hunter.")
            member = await(guild.fetch_member(payload.user_id))

            if member is not None:
                await member.remove_roles(role)
                print(f"Remove: {role}.")

            else:
                print("Member not found")
