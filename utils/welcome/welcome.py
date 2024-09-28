import random
import discord

from collections import defaultdict
import discord

# Dictionary to store recent messages
recent_messages = defaultdict(lambda: defaultdict(list))
colors = [0x1abc9c, 0x2ecc71, 0x3498db, 0x9b59b6, 0x34495e, 0x16a085, 0x27ae60, 0x2980b9, 0x8e44ad, 0x2c3e50]


async def send_welcome_message(bot, member):
    channel_id = 799183505808556044
    channel = bot.get_channel(channel_id)
    user_count = len(member.guild.members)
    color = random.choice(colors)
    embed = discord.Embed(
        title=f"Thecyberworld Community",
        description=f"Welcome {member.name} ({member.mention}) to the server! \nWe are now **{user_count}** members strong!",
        color=color
    )
    embed.add_field(name="Community Links", value="https://linktr.ee/thecyberworld", inline=False)
    embed.set_thumbnail(url=member.avatar.url)
    await channel.send(embed=embed)


async def delete_spam_message(bot, message, reason="Sending spam messages"):
    spam_keywords = [
        "sexchat", "free money", "click here", "join now", "XXX", "adult content",
        "steam", "gift", "nitro", "win big", "limited offer", "earn cash", "make money fast",
        "claim your prize", "get rich quick", "investment opportunity",
        "meet singles", "hot girls", "free trial", "exclusive deal", "act now", "urgent",
        "do not miss", "amazing offer", "click to win", "click to claim", "you have won",
        "click below", "free bitcoin", "crypto giveaway", "cash giveaway", "easy earnings",
        "no cost", "risk free", "limited time", "offer ends soon", "bonus offer"
    ]

    if any(keyword in message.content.lower() for keyword in spam_keywords):
        await message.delete()
        # await message.channel.send(f"Deleted a spam message from {message.author.name}.")

        log_channel_id = 1257606018444038247  # Replace with your log channel ID
        log_channel = bot.get_channel(log_channel_id)
        if log_channel:
            await log_channel.send(
                f"Deleted a spam message from {message.author.name} in {message.channel.name}.\n"
                f"removed: {message.content.lower()}."
            )


async def ban_for_repeated_messages(bot, message, reason="Sending the same message in multiple channels"):
    user_id = message.author.id
    content = message.content.lower()
    channel_id = message.channel.id

    if content in recent_messages[user_id] and channel_id not in recent_messages[user_id][content]:
        recent_messages[user_id][content].append(channel_id)

        # If the same message is sent in multiple channels, ban the user
        if len(recent_messages[user_id][content]) > 1:
            await message.author.ban(reason=reason)
            log_channel_id = 1257606018444038247  # Replace with your log channel ID
            log_channel = bot.get_channel(log_channel_id)
            if log_channel:
                await log_channel.send(
                    f"Banned {message.author.name} for sending the same message in multiple channels.\n"
                    f"removed: {message.content.lower()}."
                )
    else:
        recent_messages[user_id][content].append(channel_id)
