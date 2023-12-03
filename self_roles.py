import random
from utils.reactions.add_reactions import add_reaction
from utils.reactions.remove_reactions import remove_reaction
from utils.reactions.self_roles_helper import self_role_helper
from utils.reactions.self_roles_pro import self_role_pro
from utils.reactions.self_roles_team import self_role_team
from utils.reactions.self_roles_verify import self_role_verify
from utils.welcome.ready import ready
from utils.welcome.welcome import welcome_message

colors = [
    0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694,
    0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e,
    0xe67e22, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b,
    0x979c9f, 0x546e7a, 0x7289da, 0x99aab5
]


def self_roles_all(bot, discord):
    @bot.event
    async def on_ready():
        await ready(bot)

    @bot.event
    async def on_raw_reaction_add(payload):
        await add_reaction(payload)

        # Removed roles

    @bot.event
    async def on_raw_reaction_remove(payload):
        await remove_reaction(payload, bot)

    @bot.command()
    async def hello(ctx):
        await ctx.send("Hello, I am thecyberbot")

    @bot.command(pass_context=True)
    async def self_roles_cyber_teams(ctx):
        await self_role_team(ctx)

    @bot.command(pass_context=True)
    async def self_roles_cyber_pro(ctx):
        await self_role_pro(ctx)

    @bot.command(pass_context=True)
    async def self_roles_cyber_helper(ctx):
        await self_role_helper(ctx)

    @bot.command(pass_context=True)
    async def self_roles_cyber_verify(ctx):
        await self_role_verify(ctx)

    # on join welcome message
    @bot.event
    async def on_member_join(member):
        embed, channel = welcome_message(bot, random, member, discord, colors)
        await channel.send(embed=embed)


# @bot.event
# async def send_ai_reply(message):
#     print("\n\nmain:", message, "\n\n")
#     await on_message(bot, message)