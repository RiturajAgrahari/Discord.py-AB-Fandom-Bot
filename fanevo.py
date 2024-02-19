import fandom
import discord
import random

responses = ['Wait, I am finding...', 'Lemme find...', 'Hold on I almost got it..', 'Hmmmmmm...', 'I know its answer...'
    , 'Good question...', 'Let me look on wiki...', 'Here is your answer...', 'Wait for magic..',
             'You sure? ...', 'Damn I know this...', 'Wait a second...', 'I am trying to find...',
             'I am searching for your option...', 'Searching...', 'Looking for your answer...', 'I am seeking...',
             'Hitting API...', '0101101', 'Let me ask banshee', 'Vulture is typing...', '...........']

weapon = {
    'stone axe': 'https://static.wikia.nocookie.net/projectevo/images/2/2f/Stone_Axe.png/revision/latest/scale-to-width-down/90?cb=20230303214359',
    'iron axe': 'https://static.wikia.nocookie.net/projectevo/images/8/81/Iron_Axe.png/revision/latest/scale-to-width-down/90?cb=20230303214426',
    'steel axe': 'https://static.wikia.nocookie.net/projectevo/images/c/ce/Steel_Axe.png/revision/latest/scale-to-width-down/90?cb=20230303214519',
    'stone pickaxe': 'https://static.wikia.nocookie.net/projectevo/images/4/40/Stone_Pickaxe.png/revision/latest/scale-to-width-down/90?cb=20230303214543',
    'iron pickaxe': 'https://static.wikia.nocookie.net/projectevo/images/a/a2/Iron_Pickaxe.png/revision/latest/scale-to-width-down/90?cb=20230303214609',
    'steel pickaxe': 'https://static.wikia.nocookie.net/projectevo/images/d/d1/Steel_Pickaxe.png/revision/latest/scale-to-width-down/90?cb=20230303214628',
    'wooden club': 'https://static.wikia.nocookie.net/projectevo/images/c/c8/Wooden_Club.png/revision/latest/scale-to-width-down/90?cb=20230303214651',
    'iron machete': 'https://static.wikia.nocookie.net/projectevo/images/6/68/Iron_machete.png/revision/latest/scale-to-width-down/90?cb=20230303214729',
    'steel machete': 'https://static.wikia.nocookie.net/projectevo/images/9/9f/Steel_Machete.png/revision/latest/scale-to-width-down/90?cb=20230303214750',
    'bow': 'https://static.wikia.nocookie.net/projectevo/images/6/65/Bow.png/revision/latest/scale-to-width-down/90?cb=20230327104436',
    'ppsh-41': 'https://static.wikia.nocookie.net/projectevo/images/f/fa/PPSh-41_.png/revision/latest/scale-to-width-down/90?cb=20230227120414',
    'mpx': 'https://static.wikia.nocookie.net/projectevo/images/6/6e/MPX.png/revision/latest/scale-to-width-down/90?cb=20230227121754',
    'vector': 'https://static.wikia.nocookie.net/projectevo/images/2/27/Vector.png/revision/latest/scale-to-width-down/90?cb=20230227121821',
    'm4a1': 'https://static.wikia.nocookie.net/projectevo/images/a/a1/M4A1.png/revision/latest/scale-to-width-down/90?cb=20230227114332',
    'akm': 'https://static.wikia.nocookie.net/projectevo/images/6/6c/AKM.png/revision/latest/scale-to-width-down/90?cb=20230227114422',
    'aug': 'https://static.wikia.nocookie.net/projectevo/images/d/dc/AUG.png/revision/latest/scale-to-width-down/90?cb=20230227120240',
    'arx': 'https://static.wikia.nocookie.net/projectevo/images/0/06/ARX.png/revision/latest/scale-to-width-down/90?cb=20230227114555',
    'kar98k': 'https://static.wikia.nocookie.net/projectevo/images/6/65/Kar98k.png/revision/latest/scale-to-width-down/90?cb=20230227113913',
    'm700': 'https://static.wikia.nocookie.net/projectevo/images/6/6a/M700.png/revision/latest/scale-to-width-down/90?cb=20230227114127',
    'barrett': 'https://static.wikia.nocookie.net/projectevo/images/f/f3/Barrett.png/revision/latest/scale-to-width-down/90?cb=20230227114241',
    'ameli': 'https://static.wikia.nocookie.net/projectevo/images/b/b3/Ameli.png/revision/latest/scale-to-width-down/90?cb=20230227120329',
    'mk46': 'https://static.wikia.nocookie.net/projectevo/images/b/b5/MK46.png/revision/latest/scale-to-width-down/90?cb=20230227121727',
    'm1897': 'https://static.wikia.nocookie.net/projectevo/images/1/16/M1897.png/revision/latest/scale-to-width-down/90?cb=20230227115519',
    'browning 27': 'https://static.wikia.nocookie.net/projectevo/images/e/e0/Browning_27.png/revision/latest/scale-to-width-down/90?cb=20230227114908',
    'saiga-12': 'https://static.wikia.nocookie.net/projectevo/images/b/b9/Saiga-12.png/revision/latest/scale-to-width-down/90?cb=20230227121849',
    'c4': 'https://static.wikia.nocookie.net/projectevo/images/a/a7/C4.png/revision/latest/scale-to-width-down/90?cb=20230226092534',
    'rocket': 'https://static.wikia.nocookie.net/projectevo/images/f/fb/Rocket.png/revision/latest/scale-to-width-down/90?cb=20230303215032',
    'dynamite bundle': 'https://static.wikia.nocookie.net/projectevo/images/f/fc/Dynamite.png/revision/latest/scale-to-width-down/90?cb=20230226092426',
    'frag grenade': 'https://static.wikia.nocookie.net/projectevo/images/6/6b/Frag_Grenade.png/revision/latest/scale-to-width-down/90?cb=20230222030940',
    'flash bang': 'https://static.wikia.nocookie.net/projectevo/images/e/e4/Flash_Bang.png/revision/latest/scale-to-width-down/90?cb=20230316094945',
    'smoke grenade': 'https://static.wikia.nocookie.net/projectevo/images/d/d5/Smoke_Grenade.png/revision/latest/scale-to-width-down/90?cb=20230303215317',
    'rocket launcher': 'https://static.wikia.nocookie.net/projectevo/images/8/84/Rocket_launcher.png/revision/latest/scale-to-width-down/90?cb=20230227122328',
    'flare gun': 'https://static.wikia.nocookie.net/projectevo/images/5/57/Flare_Gun.png/revision/latest/scale-to-width-down/90?cb=20230227115205'
    }

NPCs = {
    'normie': 'https://static.wikia.nocookie.net/projectevo/images/f/f0/Normie1.png/revision/latest/scale-to-width-down/350?cb=20230330153339',
    'nurser': 'https://static.wikia.nocookie.net/projectevo/images/c/c5/Nurser_icon.png/revision/latest/scale-to-width-down/350?cb=20230330114211',
    'trooper': 'https://static.wikia.nocookie.net/projectevo/images/2/23/Trooper_icon.png/revision/latest/scale-to-width-down/350?cb=20230330115113',
    'puker': 'https://static.wikia.nocookie.net/projectevo/images/9/93/Puker_icon.png/revision/latest/scale-to-width-down/350?cb=20230330114808',
    'red belly': 'https://static.wikia.nocookie.net/projectevo/images/4/47/Red_Belly_icon.png/revision/latest/scale-to-width-down/350?cb=20230324143858',
    'mobber': 'https://static.wikia.nocookie.net/projectevo/images/8/8c/Mobber_icon.png/revision/latest/scale-to-width-down/350?cb=20230330114159',
    'mob captain': 'https://static.wikia.nocookie.net/projectevo/images/c/c0/Mob_Captain_icon.png/revision/latest/scale-to-width-down/350?cb=20230330114141',
    'dozer': 'https://static.wikia.nocookie.net/projectevo/images/5/5d/Dozer_icon.png/revision/latest/scale-to-width-down/350?cb=20230330113922',
    'scoper': 'https://static.wikia.nocookie.net/projectevo/images/0/08/Scoper_icon.png/revision/latest/scale-to-width-down/350?cb=20230330115043',
    'mammon': 'https://static.wikia.nocookie.net/projectevo/images/e/eb/Mammon_icon.png/revision/latest/scale-to-width-down/350?cb=20230330114119',
    'rager': 'https://static.wikia.nocookie.net/projectevo/images/9/9f/Rager_icon.png/revision/latest/scale-to-width-down/350?cb=20230330114900',
    'rage captain': 'https://static.wikia.nocookie.net/projectevo/images/d/d4/Rage_Captain_icon.png/revision/latest/scale-to-width-down/350?cb=20230330114843',
    'elite scoper': 'https://static.wikia.nocookie.net/projectevo/images/c/cc/Elite_Scoper_icon.png/revision/latest/scale-to-width-down/350?cb=20230330113905',
    'goyle': 'https://static.wikia.nocookie.net/projectevo/images/d/d7/Goyle_icon.png/revision/latest/scale-to-width-down/350?cb=20230330113947',
    'zed': 'https://static.wikia.nocookie.net/projectevo/images/c/c9/Zed_icon.png/revision/latest/scale-to-width-down/350?cb=20230330115143',
    "panzer": 'https://static.wikia.nocookie.net/projectevo/images/1/16/Panzer_icon.png/revision/latest/scale-to-width-down/350?cb=20230330114750',
    'sicario': 'https://static.wikia.nocookie.net/projectevo/images/e/e6/Sicario_icon.png/revision/latest/scale-to-width-down/350?cb=20230330115100',
    'kane': 'https://static.wikia.nocookie.net/projectevo/images/1/1b/Kane_icon.png/revision/latest/scale-to-width-down/350?cb=20230330114003',
    'vulture': 'https://static.wikia.nocookie.net/projectevo/images/f/f3/Vulture_icon.png/revision/latest/scale-to-width-down/350?cb=20230330115129',
    'banshee': 'https://static.wikia.nocookie.net/projectevo/images/e/ea/Banshee_icon.png/revision/latest/scale-to-width-down/350?cb=20230330113840',
    'night owl': 'https://static.wikia.nocookie.net/projectevo/images/e/e8/Nightowl.png/revision/latest/scale-to-width-down/350?cb=20230607143240'
}

MY_GUILD = discord.Object(id='your_guild_id')


async def infobox_monu(infobox, page):
    print(infobox)
    embed = discord.Embed(
        title='INFOBOX',
        description=infobox[0],
        color=discord.Color.from_str('#bf4946'),
    )
    try:
        embed.add_field(name=infobox[1],
                        value=f'{infobox[2]}  :  {infobox[3]}\n'
                              f'{infobox[4]}  :  {infobox[5]}\n'
                              f'{infobox[6]}  :  {infobox[7]}\n'
                              f'{infobox[8]}  :  {infobox[9]}\n'
                              f'{infobox[10]}  :  {infobox[11]}\n'
                              f'{infobox[12]}  :  {infobox[13]}, '
                              f'{infobox[16]}',
                        inline=False)
    except:
        embed.add_field(name=infobox[1],
                        value=f'{infobox[2]}  :  {infobox[3]}\n'
                              f'{infobox[4]}  :  {infobox[5]}\n'
                              f'{infobox[6]}  :  {infobox[7]}\n'
                              f'{infobox[8]}  :  {infobox[9]}\n'
                              f'{infobox[10]}  :  {infobox[11]}\n'
                              f'{infobox[12]}  :  {infobox[13]}, ',
                        inline=False)

    return embed


async def attachments(attachment, name, page):
    print(attachment)
    embed2 = discord.Embed(
        title='ATTACHMENT',
        color=discord.Color.from_str('#bf4946'),
    )
    embed2.url = page.url
    embed2.set_thumbnail(url=weapon[name])
    for i in range(3, len(attachment), 2):
        embed2.add_field(name=attachment[i],
                         value=attachment[i + 1],
                         inline=False)

    return embed2


async def infobox_data(infobox, page):
    embed3 = discord.Embed(
        title='INFOBOX',
        description=infobox[0],
        color=discord.Color.from_str('#bf4946'),
    )
    embed3.url = page.url
    embed3.set_thumbnail(url=weapon[str(infobox[0]).lower()])

    if infobox[8] == 'Weapon Stats':
        embed3.add_field(name=infobox[1],
                         value=f'{infobox[2]}  :  {infobox[3]}\n'
                               f'{infobox[4]}  :  {infobox[5]}\n'
                               f'{infobox[6]}  :  {infobox[7]}',
                         inline=False)

        if infobox[11] == "Delay":
            embed3.add_field(name=infobox[8],
                             value=f'{infobox[9]}  :  {infobox[10]}\n'
                                   f'{infobox[11]}  :  {infobox[12]}',
                             inline=False)

            if infobox[19] == 'Workbench':
                embed3.add_field(name=infobox[13],
                                 value=f'{infobox[14]}  :  {infobox[15]}\n'
                                       f'{infobox[16]}  :  {infobox[17]}\n'
                                       f'{infobox[18]}  :  {infobox[19]}',
                                 inline=False)

            else:
                embed3.add_field(name=infobox[12],
                                 value=f'{infobox[13]}  :  {infobox[14]}\n'
                                       f'{infobox[15]}  :  {infobox[16]}',
                                 inline=False)

        else:
            embed3.add_field(name=infobox[8],
                             value=f'{infobox[9]}  :  {infobox[10]}\n',
                             inline=False)

            if infobox[16] == 'Workbench':
                embed3.add_field(name=infobox[12],
                                 value=f'{infobox[13]}  :  {infobox[14]}\n'
                                       f'{infobox[15]}  :  {infobox[16]}\n'
                                       f'{infobox[17]}  :  {infobox[18]}',
                                 inline=False)

            else:
                embed3.add_field(name=infobox[12],
                                 value=f'{infobox[13]}  :  {infobox[14]}\n'
                                       f'{infobox[15]}  :  {infobox[16]}',
                                 inline=False)




    else:
        embed3.add_field(name=infobox[1],
                         value=f'{infobox[2]}  :  {infobox[3]}\n'
                               f'{infobox[4]}  :  {infobox[5]}\n'
                               f'{infobox[6]}  :  {infobox[7]}\n'
                               f'{infobox[8]}  :  {infobox[9]}',
                         inline=False)

        embed3.add_field(name=infobox[10],
                         value=f'{infobox[11]}  :  {infobox[12]}\n'
                               f'{infobox[13]}  :  {infobox[14]}\n'
                               f'{infobox[15]}  :  {infobox[16]}\n'
                               f'{infobox[17]}  :  {infobox[18]}\n'
                               f'{infobox[19]}  :  {infobox[20]}\n'
                               f'{infobox[21]}  :  {infobox[22]}',
                         inline=False)

        if infobox[28] == 'Workbench':
            embed3.add_field(name=infobox[23],
                             value=f'{infobox[24]}  :  {infobox[25]}\n'
                                   f'{infobox[26]}  :  {infobox[27]}\n'
                                   f'{infobox[28]}  :  {infobox[29]}',
                             inline=False)

        else:
            embed3.add_field(name=infobox[23],
                             value=f'{infobox[24]}  :  {infobox[25]}\n'
                                   f'{infobox[26]}  :  {infobox[27]}',
                             inline=False)

    return embed3


async def infobox_npc(infobox, zombie, page):
    embed = discord.Embed(
        title='INFOBOX',
        description=infobox[0],
        color=discord.Color.red(),
    )
    embed.url = page.url
    embed.set_thumbnail(url=NPCs[zombie])
    if zombie != 'normie':
        embed.add_field(name=infobox[1],
                        value=f'{infobox[2]}  :  {infobox[3]}\n'
                              f'{infobox[4]}  :  {infobox[5]}\n'
                              f'{infobox[6]}  :  {infobox[7]}\n'
                              f'{infobox[8]}  :  {infobox[9]}',
                        inline=False)
        embed.add_field(name=infobox[10],
                        value=f'{infobox[11]}  :  {infobox[12]}\n'
                              f'{infobox[13]}  :  {infobox[14]}\n'
                              # f'{infobox[15]}  :  {infobox[16]}\n'
                              f'{infobox[15]}  :  {infobox[16]}',
                        inline=False)

        return embed

    else:
        embed.add_field(name=infobox[25],
                        value=f'{infobox[26]}  :  {infobox[27]}\n'
                              f'{infobox[28]}  :  {infobox[29]}\n'
                              f'{infobox[30]}  :  {infobox[31]}\n'
                              f'{infobox[32]}  :  {infobox[33]}',
                        inline=False)
        embed.add_field(name=infobox[34],
                        value=f'{infobox[35]}  :  {infobox[36]}\n'
                              f'{infobox[37]}  :  {infobox[38]}\n'
                              f'{infobox[39]}  :  {infobox[40]}\n'
                              f'{infobox[41]}  :  {infobox[42]}',
                        inline=False)

        return embed


async def weapons_main(weapon_name, category, interaction):
    response = responses[random.randint(0, len(responses))]
    fandom.set_wiki('projectevo')
    search = fandom.search(weapon_name, results=1)
    name = str(weapon_name).lower()
    try:
        await interaction.response.send_message(response, ephemeral=True)
        page_name = search[0][0]
        page_no = search[0][1]
        page = fandom.page(title=page_name)
        page2 = fandom.page(pageid=page_no)
        print(f'[fanevo.py--588--]{page == page2}')
        try:
            content = page.content
            print(f'[fanevo.py--591--] content = {content}')
            section = content['sections']
            print(f'[fanevo.py--593--] content = {section}')
            if category == 'ALL':
                embed = discord.Embed(
                    title=content['title'],
                    description=content['content'],
                    color=discord.Color.from_str('#bf4946'),
                )
                embed.url = page.url
                embed.set_thumbnail(url=weapon[name])
                for i in range(0, len(section)):
                    if section[i]['title'] == 'Attachments':
                        data = section[i]['content']
                        attachment = str(data).split('\n')
                        print(attachment)
                        embed2 = await attachments(attachment, name, page)
                        await interaction.followup.send(embed=embed2, ephemeral=True)
                        # await interaction.followup.send(embed=A, ephemeral=True)

                    else:
                        embed.add_field(name=section[i]['title'],
                                        value=section[i]['content'],
                                        inline=False)
                # await interaction.followup.send(embed=embed, ephemeral=True)

                try:
                    infobox = str(content['infobox']).split('\n')
                    embed3 = await infobox_data(infobox, page)
                    await interaction.followup.send(embed=embed, ephemeral=True)
                    await interaction.followup.send(embed=embed3, ephemeral=True)

                except Exception as e:
                    print(f"[fanevo.py--624--] {e}")
            else:
                if str(category).lower().startswith('attachment'):
                    try:
                        data = section[4]['content']
                        attachment = str(data).split('\n')
                        print(attachment)
                        A = await attachments(attachment, name, page)
                        await interaction.edit_original_response(content="", embed=A)
                    except Exception as e:
                        print(f'[fanevo.py--634--] : {e}')
                        await interaction.edit_original_response(content=f"{weapon_name} doesn't have any attachments")
                elif str(category).lower() == 'infobox':
                    data = content['infobox']
                    infobox = str(data).split('\n')
                    data = await infobox_data(infobox, page)
                    await interaction.edit_original_response(content="", embed=data)
                else:
                    for j in range(0, len(section)):
                        print(category)
                        print(str(section[j]['title']).lower())
                        if str(section[j]['title']).lower() == str(category).lower():
                            embed = discord.Embed(
                                title=section[j]['title'],
                                description=section[j]['content'],
                                color=discord.Color.from_str('#bf4946'),
                            )
                            await interaction.edit_original_response(content="", embed=embed)
                            break
                        else:
                            print('category not matched!')
                    else:
                        await interaction.edit_original_response(content=f"{interaction.user.mention}"
                                                                         f" Category doesn't exits!\n"
                                                                         f"Availaible categories are:\n"
                                                                         f"--> crafting,\n"
                                                                         f"--> researching,\n"
                                                                         f"--> recycling,\n"
                                                                         f"--> drop location,\n"
                                                                         f"--> infobox,\n"
                                                                         f"--> attachments")
        except Exception as e:
            print(f'[fanevo.py--666--]{e}')
    except:
        await interaction.response.send_message(f'Their is no such type of category for [{weapon_name}] in fandom',
                                                ephemeral=True)


async def Monument_main(Monument, category, user, interaction):
    response = responses[random.randint(0, len(responses))]
    fandom.set_wiki('projectevo')
    search = fandom.search(Monument, results=1)
    try:
        await interaction.response.send_message(response, ephemeral=True)
        page_name = search[0][0]
        page_no = search[0][1]
        page = fandom.page(title=page_name)
        page2 = fandom.page(pageid=page_no)
        print(page == page2)
        try:
            content = page.content
            section = content['sections']
            print(content)
            print(section)
            if category == 'ALL':
                embed = discord.Embed(
                    title=content['title'],
                    description=content['content'],
                    color=discord.Color.from_str('#bf4946'),
                )
                embed.url = page.url
                for i in range(0, len(section)):
                    if section[i]['title'] != 'Zombies':
                        embed.add_field(name=section[i]['title'],
                                        value=section[i]['content'],
                                        inline=False)
                    else:
                        data = str(section[i]['content']).split('GUIDE')
                        embed.add_field(name=section[i]['title'],
                                        value=data[0],
                                        inline=False)
                try:
                    data = content['infobox']
                    infobox = str(data).split('\n')
                    data = await infobox_monu(infobox, page)
                    await interaction.followup.send(embed=embed, ephemeral=True)
                    await interaction.followup.send(embed=data, ephemeral=True)
                except:
                    print("infobox error")
            else:
                if str(category).lower() == 'infobox':
                    data = content['infobox']
                    infobox = str(data).split('\n')
                    data = await infobox_monu(infobox, page)
                    await interaction.edit_original_response(content="", embed=data)
                else:
                    for j in range(0, len(section)):
                        print(category)
                        print(str(section[j]['title']).lower())
                        if str(section[j]['title']).lower() == str(category).lower():
                            embed = discord.Embed(
                                title=section[j]['title'],
                                description=section[j]['content'],
                                color=discord.Color.from_str('#bf4946'),
                            )
                            await interaction.edit_original_response(content="", embed=embed)
                            break
                        else:
                            print('category not matched!')
                    else:
                        await interaction.edit_original_response(content=f"{interaction.user.mention}"
                                                                         f" Category doesn't exits!\n"
                                                                         f"Availaible categories are:\n"
                                                                         f"--> layout,\n"
                                                                         f"--> loot,\n"
                                                                         f"--> zombies,\n"
                                                                         f"--> infobox,\n")
        except:
            print(f'Template in page content')
    except:
        await interaction.response.send_message(f'Their is no such type of category in [{Monument}] in fandom',
                                                ephemeral=True)


async def NPC_main(NPC, category, user, interaction):
    response = responses[random.randint(0, len(responses))]
    fandom.set_wiki('projectevo')
    search = fandom.search(NPC, results=1)
    npc_name = str(NPC).lower()
    try:
        await interaction.response.send_message(response, ephemeral=True)
        page_name = search[0][0]
        page_no = search[0][1]
        page = fandom.page(title=page_name)
        page2 = fandom.page(pageid=page_no)
        print(page == page2)
        try:
            content = page.content
            section = content['sections']
            print(content)
            print(section)
            if category == 'ALL':
                embed = discord.Embed(
                    title=page_name,
                    description=page.summary,
                    color=discord.Color.red()
                )
                embed.url = page.url
                print(NPCs[npc_name])
                embed.set_thumbnail(url=NPCs[npc_name])
                for i in range(0, len(section)):
                    if section[i]['title'] != 'Map':
                        data = str(section[i]['content']).split('GUIDE')
                        embed.add_field(name=section[i]['title'],
                                        value=data[0],
                                        inline=False)
                    else:
                        print('map detail!!')

                await interaction.followup.send(embed=embed, ephemeral=True)
                data = content['infobox']
                infobox = str(data).split('\n')
                data = await infobox_npc(infobox, npc_name, page)
                await interaction.followup.send(embed=data, ephemeral=True)
                print(page.images)

            else:
                if str(category).lower() == 'infobox':
                    data = content['infobox']
                    infobox = str(data).split('\n')
                    data = await infobox_npc(infobox, npc_name, page)
                    await interaction.edit_original_response(content="", embed=data)
                else:
                    for j in range(0, len(section)):
                        print(category)
                        print(str(section[j]['title']).lower())
                        if str(section[j]['title']).lower() == str(category).lower():
                            embed = discord.Embed(
                                title=section[j]['title'],
                                description=section[j]['content'],
                                color=discord.Color.from_str('#bf4946'),
                            )
                            await interaction.edit_original_response(content="", embed=embed)
                            break
                        else:
                            print('category not matched!')
                    else:
                        await interaction.edit_original_response(content=f"{interaction.user.mention}"
                                                                         f" Category doesn't exits!\n"
                                                                         f"Availaible categories are:\n"
                                                                         f"--> found,\n"
                                                                         f"--> possible drop,\n"
                                                                         f"--> infobox,\n")

        except Exception as e:
            print(e)
            print('Template in page content')
    except:
        await interaction.response.send_message(f"{interaction.user.mention} Page not exist!", ephemeral=True)


async def send_answer(questions, interaction):
    if questions == 'How to change language in game?':
        embed = discord.Embed(
            title=questions,
            color=discord.Color.from_str('#bf4946'),
        )
        embed.set_image(
            url='https://cdn.discordapp.com/attachments/986104805795725343/1115598919183908894/ezgif.com-optimize.gif')
        embed.set_footer(text=f"Requested by: {interaction.user}")
        await interaction.response.send_message(embed=embed, ephemeral=False)

    elif questions == 'When will the game release on iOS?':
        embed = discord.Embed(
            title=questions,
            description=f"For now, the game is only available on Android. If you are on iOS, do not worry. Mission EVO will be available on both iOS and Android in future releases.",
            color=discord.Color.from_str('#bf4946'),
        )
        embed.set_footer(text=f"Requested by: {interaction.user}")
        await interaction.response.send_message(embed=embed, ephemeral=False)

    elif questions == 'How long does it take for loot to respawn in vaults?':
        embed = discord.Embed(
            title=questions,
            description=f"<:greenkey:1062408655653322793> Green Vault --> 30 minutes\n"
                        f"<:yellowkey:1062408611189501962> Yellow Vault --> 1 hour\n"
                        f"<:redkey:1062408656735457382> Red Vault --> 1 hour",
            color=discord.Color.from_str('#bf4946'),
        )
        embed.set_footer(text=f"Requested by: {interaction.user}")
        await interaction.response.send_message(embed=embed, ephemeral=False)
    elif questions == 'How to make main territory?':
        embed = discord.Embed(
            title=questions,
            color=discord.Color.from_str('#bf4946'),
        )
        embed.add_field(
            name='Make a temporary territory',
            value='Make a temporary territory and shift your loot their to save it from despawning.\n'
                  'Note: Temporary territory are durable upto 2 hours',
            inline=False
        )
        embed.add_field(
            name='Delete your main territory',
            value='You can directly delete your main territory via map, watch the tutorial below.',
            inline=False
        )
        embed.set_image(url='')
        embed.add_field(
            name='Build main territory',
            value='Now the territory you will build is your main territory and now you can shift your loot to'
                  'main territory',
            inline=False
        )
        await interaction.response.send_message(embed=embed)
    else:
        print("what question?")
