import discord
import os

from typing import Literal
from dotenv import load_dotenv

from discord import app_commands

from options import *

load_dotenv()

MAIN_GUILD_ID = int(os.getenv("MAIN_SERVER_ID"))
# TEST_GUILD_ID = int(os.getenv("TEST_SERVER_ID"))

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
        # second_guild = discord.Object(id=TEST_GUILD_ID)
        # if second_guild.id != MAIN_GUILD_ID:
        #     self.tree.copy_global_to(guild=second_guild)
        #     await self.tree.sync(guild=second_guild)


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


@client.tree.command(name="medicine", description="Select a medicine to see its detail!")
async def medicine(interaction: discord.Interaction, medicine: Literal['Fast-Acting Painkill', 'EX Painkiller', 'AP Painkiller', 'Anti-Inflam Painkill', 'Cond. Painkiller', 'Energy Drink', 'Quick Bandage', 'Field Bandage', 'OPM Bandage', 'Simple Surgical Pack', 'Standard Military Su', 'TMK Military Surgica', 'STO Battlefield Surg', 'G-96 Nebulizer', 'Standard Military Fi', 'E3 Military Medkit', 'Simple First Aid Box', '926 Rapid First Aid ', '100D Battlefield Med', 'STO First Aid Set', 'TMK Field Medkit', 'Regen Booster', 'Regen Injection', 'Endurance Booster', 'Endurance Injection', 'Strength Booster', 'Str. Injection']):
    print(f'{interaction.user} is checking {medicine} Medicine...')
    # await weapons_main(weapon_name, category, interaction)


@client.tree.command(name="wiki-monuments", description="Select a monument to see its detail!")
async def monuments(interaction: discord.Interaction, monument: Literal['test', 'Port Tackson', 'Silver City', 'Port Harlow', 'River City', 'Mt. Bedford', 'Cape Hattersborne', 'Riverbank Retreat', "Nelson's Lumberyard", 'Red Pine Ranch', 'Maynard Loggers', 'Meekers Mill', 'Cloudsville', 'Point Slope', 'Alpine Mine', 'Littleton', 'Raonoke'], category: Literal['layout', 'loot', 'zombies', 'infobox', 'ALL']):
    print(f'{interaction.user} is checking {monument}...')
    print(category)
    user_id = interaction.user.id
    user = await client.fetch_user(user_id)
    await Monument_main(monument, category, user, interaction)


@client.tree.command(name="wiki-npc", description="Select a NPC to see its detail!")
async def npc(interaction: discord.Interaction, npc: Literal['Normie', 'Nurser', 'Trooper', 'Puker', 'Red Belly', 'Mobber', 'Mob Captain', 'Dozer', 'Scoper', 'Mammon', 'Rager', 'Rage Captain', 'Elite Scoper', 'Goyle', 'Zed', 'Panzer', 'Sicario', 'Kane', 'Banshee', 'Vulture', 'Night Owl'], category: Literal['infobox', 'found', 'possible drop', 'ALL']):
    print(f'{interaction.user} is checking {npc}...')
    print(category)
    user_id = interaction.user.id
    user = await client.fetch_user(user_id)
    await NPC_main(npc, category, user, interaction)


@client.tree.command(name="wiki-faq", description="Select your question!")
async def question(interaction: discord.Interaction, questions: Literal['How to change language in game?',
                                                                        'When will the game release on iOS?',
                                                                        'How long does it take for loot to respawn in vaults?']):
    print(f'{interaction.user} question is {questions}')
    await send_answer(questions, interaction)


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
    message = args[0] # Gets the message object
    await send_error(__file__, event, 'Their is some error!')


client.run(os.getenv("TOKEN"))
