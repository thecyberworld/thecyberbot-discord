import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
import random
from utils.welcome import welcome_message
from utils.reactions.remove_reactions import remove_react
from utils.reactions.add_reactions import add_reactions
from utils.reactions.self_roles_team import self_role_team
from utils.reactions.self_roles_pro import self_role_pro
from utils.reactions.self_roles_helper import self_role_helper
from utils.reactions.self_roles_verify import self_role_verify
from utils.reactions.self_roles_verify import self_role_verify
from utils.welcome.ready import ready

colors = [
    0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694,
    0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e,
    0xe67e22, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b,
    0x979c9f, 0x546e7a, 0x7289da, 0x99aab5
]

load_dotenv()

TOKEN = os.getenv('TOKEN')

def run_discord_bot():
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    bot = discord.Client(intents=intents)
    bot = commands.Bot(command_prefix='!', intents=intents)
    self_roles_1_id = 1027668015791214673
    self_roles_cyber_team_id = 1031750672141537352
    self_roles_helper_id = 1031755073128247397
    self_roles_verify_id = 1059559943071608853

    # self_roles_pro_id = 1027668015791214673

    @bot.event
    async def on_ready():
        
        await ready(bot)

    @bot.event
    async def on_raw_reaction_add(payload):
        our_message_id = self_roles_1_id
        await add_reactions(our_message_id, payload, self_roles_cyber_team_id, self_roles_helper_id, self_roles_verify_id)

    # Removed roles
    @bot.event
    async def on_raw_reaction_remove(payload):
        our_message_id = self_roles_1_id
        await remove_react(our_message_id, payload, bot, self_roles_cyber_team_id, self_roles_helper_id)

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

    # Remember to run your bot with your personal TOKEN
    bot.run(TOKEN)
