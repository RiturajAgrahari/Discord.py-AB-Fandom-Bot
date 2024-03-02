import discord
import os

from typing import Literal
from dotenv import load_dotenv

from discord import app_commands

from options import get_category, DATA
from basic import get_average

load_dotenv()

MAIN_GUILD_ID = int(os.getenv("MAIN_SERVER_ID"))
TEST_GUILD_ID = int(os.getenv("TEST_SERVER_ID"))

class MyClient(discord.Client):
    def __init__(self, *, intents:discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Set up command tree for the first guild
        first_guild = discord.Object(id=MAIN_GUILD_ID)
        self.tree.copy_global_to(guild=first_guild)
        await self.tree.sync(guild=first_guild)

        # Set up command tree for the second guild
        second_guild = discord.Object(id=TEST_GUILD_ID)
        if second_guild.id != MAIN_GUILD_ID:
            self.tree.copy_global_to(guild=second_guild)
            await self.tree.sync(guild=second_guild)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(f'Your Arena Breakout bot in succesfully started as {client.user} (ID: {client.user.id})')
    print('-----')


@client.event
async def on_message(message):
    # Checks if the message is recieved in DM
    if message.channel.type == discord.ChannelType.private:
        print(f'DM --> [{message.author}] : {message.content}')

    # Check if the message author is not client itself
    if message.author == client.user:
        pass

    # Message in server channels
    else:
        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        channel = str(message.channel.name)
        guild_name = message.guild.name
        # print(f'[channel: {channel}] --> {username}: {user_message}')

        if channel == 'rpg':
            print('success')


@client.tree.command(name="wiki-food", description="Select a food item to check its detail!")
async def food(interaction: discord.Interaction, item: Literal[DATA['FOOD']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)


@client.tree.command(name="wiki-beverage", description="Select a beverage item to check its detail!")
async def beverage(interaction: discord.Interaction, item: Literal[DATA['BEVERAGES']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)


@client.tree.command(name="wiki-tier-1-body-armor", description="Select a armor to check its detail!")
async def tierOneArmor(interaction: discord.Interaction, item: Literal[DATA['Tier 1 Body Armor']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)


@client.tree.command(name="wiki-tier-2-body-armor", description="Select a armor to check its detail!")
async def tierTwoArmor(interaction: discord.Interaction, item: Literal[DATA['Tier 2 Body Armor']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)

@client.tree.command(name="wiki-tier-3-body-armor", description="Select a armor to check its detail!")
async def TierThreeArmor(interaction: discord.Interaction, item: Literal[DATA['Tier 3 Body Armor']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)

@client.tree.command(name="wiki-tier-4-body-armor", description="Select a armor to check its detail!")
async def TierFourArmor(interaction: discord.Interaction, item: Literal[DATA['Tier 4 Body Armor']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)

@client.tree.command(name="wiki-tier-5-body-armor", description="Select a armor to check its detail!")
async def TierFiveArmor(interaction: discord.Interaction, item: Literal[DATA['Tier 5 Body Armor']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)

@client.tree.command(name="wiki-tier-6-body-armor", description="Select a armor to check its detail!")
async def tierSixArmor(interaction: discord.Interaction, item: Literal[DATA['Tier 6 Body Armor']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)

@client.tree.command(name="wiki-tier-1-helmet", description="Select a helmet to check its detail!")
async def tierOneHelmet(interaction: discord.Interaction, item: Literal[DATA['Tier 1 Helmets']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)

@client.tree.command(name="wiki-tier-2-helmet", description="Select a helmet to check its detail!")
async def tierTwoHelmet(interaction: discord.Interaction, item: Literal[DATA['Tier 2 Helmets']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)
@client.tree.command(name="wiki-tier-3-helmet", description="Select a helmet to check its detail!")
async def tierThreeHelmet(interaction: discord.Interaction, item: Literal[DATA['Tier 3 Helmets']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)
@client.tree.command(name="wiki-tier-4-helmet", description="Select a helmet to check its detail!")
async def tierFourHelmet(interaction: discord.Interaction, item: Literal[DATA['Tier 4 Helmets']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)
@client.tree.command(name="wiki-tier-5-helmet", description="Select a helmet to check its detail!")
async def tierFiveHelmet(interaction: discord.Interaction, item: Literal[DATA['Tier 5 Helmets']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)
@client.tree.command(name="wiki-tier-6-helmet", description="Select a helmet to check its detail!")
async def tierSixHelmet(interaction: discord.Interaction, item: Literal[DATA['Tier 6 Helmets']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)

@client.tree.command(name="wiki-throwables", description="Select a throwable to check its detail!")
async def throwables(interaction: discord.Interaction, item: Literal[DATA['THROWABLES']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)

@client.tree.command(name="wiki-headsets", description="Select a headset to check its detail!")
async def headsets(interaction: discord.Interaction, item: Literal[DATA['HEADSETS']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)

@client.tree.command(name="wiki-masks", description="Select a mask to check its detail!")
async def masks(interaction: discord.Interaction, item: Literal[DATA['MASKS']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)

@client.tree.command(name="wiki-chest-rigs", description="Select a chest rig to check its detail!")
async def chestRigs(interaction: discord.Interaction, item: Literal[DATA['CHEST RIGS']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)

@client.tree.command(name="wiki-armored-rigs", description="Select a armored rig to check its detail!")
async def armoredRigs(interaction: discord.Interaction, item: Literal[DATA['ARMORED RIGS']]):
    await interaction.response.defer(ephemeral=True)
    embed = await get_average(item)
    await interaction.followup.send(embed=embed, ephemeral=True)



async def get_avatar_url(interaction):
    try:
        user_avatar_url = interaction.user.avatar.url
        return user_avatar_url
    except:
        default_avatar_url = 'https://cdn.discordapp.com/attachments/1171092440233541632/1176439824622833764/Untitled.png?ex=656edff7&is=655c6af7&hm=3e2cd8767c426187fbfc3171749ccf0158152f94a9b64f5acb3ae0a868a907c5&'
        return default_avatar_url


# Last Optimization [19-01-2024] --> Need Relocation
async def send_error(file, function_name, error, server='Anonymous'):
    embed = discord.Embed(title=f'{server} Server',
        description=file,
        color=discord.Color.red()
    )
    embed.add_field(
        name=function_name,
        value=error,
        inline=False
    )
    user = await client.fetch_user(568179896459722753)
    await user.send(embed=embed)

@client.event
async def on_error(event, *args, **kwargs):
    # message = args[0] # Gets the message object
    await send_error(__file__, event, 'Their is some error!')


client.run(os.getenv("TOKEN"))
