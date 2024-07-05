import discord


embed = discord.Embed(
    title="Features that we provide",
    description="This bot provides comprehensive information on in-game items! We're constantly adding new"
                " categories and updating the database with the latest version. While some categories might"
                " not be available yet, stay tuned – we're working hard to expand the bot's capabilities.\n\n"
                "** </wiki-ammunition--44:1258679814282543138> :** For detail related to .44 ammo\n"
                "** </wiki-ammunition--45:1258679814282543137> :** For detail related to .45 ammo\n"
                "** </wiki-ammunition--338:1258679814282543136> :** For detail related to .338 ammo\n"
                "** </wiki-ammunition-5-7x28mm:1258679814282543142> :** For detail related to 5.7x28mm ammo\n"
                "** </wiki-ammunition-5-45x39mm:1258679814282543140> :** For detail related to 5.45x39mm ammo\n"
                "** </wiki-ammunition-5-56x45mm:1258679814642995332> :** For detail related to 5.56x45mm ammo\n"
                "** </wiki-ammunition-7-62x39mm:1258679814642995334> :** For detail related to 7.62x39mm ammo\n"
                "** </wiki-ammunition-7-62x51mm:1258679814282543143> :** For detail related to 7.62x51mm ammo\n"
                "** </wiki-ammunition-7-62x54mm:1258679814642995333> :** For detail related to 7.62x54mm ammo\n"
                "** </wiki-ammunition-9x19mm:1258679814642995331> :** For detail related to 9x19mm ammo\n"
                "** </wiki-ammunition-9x39mm:1258679814282543141> :** For detail related to 9x39mm ammo\n"
                "** </wiki-ammunition-12-7x99mm:1258679814282543139> :** For detail related to 12-7x99mm ammo\n"
                "** </wiki-armored-rigs:1214195293294436362> :** For detail related to armored-rigs\n"
                "** </wiki-assault-rifles:1214195292581265419> :** For detail related to assault-rifles\n"
                "** </wiki-beverage:1258679814642995340> :** For detail related to beverages\n"
                "** </wiki-carbines:1258679814642995337> :** For detail related to carbines\n"
                "** </wiki-chest-rigs:1214195292854026310> :** For detail related to chest-rigs\n"
                "** </wiki-food:1214195292581265418> :** For detail related to foods\n"
                "** </wiki-handguns:1258679814802505801> :** For detail related to handguns\n"
                "** </wiki-headsets:1214195292854026308> :** For detail related to headsets\n"
                "** </wiki-machine-gun:1258679814642995338> :** For detail related to machine-gun\n"
                "** </wiki-marksman-rifles:1258679814642995336> :** For detail related to marksman-rifles\n"
                "** </wiki-masks:1214195292854026309> :** For detail related to masks\n"
                "** </wiki-shotguns:1258679814642995339> :** For detail related to shotguns\n"
                "** </wiki-sniper-rifles:1258679814642995335> :** For detail related to sniper-rifles\n"
                "** </wiki-submachine-guns:1258679814802505799> :** For detail related to submachine-guns\n"
                "** </wiki-throwables:1214195292854026307> :** For detail related to throwables\n"
                "** </wiki-tier-1-body-armor:1214195292581265420> :** For detail related to tier-1-body-armor\n"
                "** </wiki-tier-1-helmet:1214195292581265426> :** For detail related to tier-1-helmet\n"
                "** </wiki-tier-2-body-armor:1214195292581265421> :** For detail related to tier-2-body-armor\n"
                "** </wiki-tier-2-helmet:1214195292854026301> :** For detail related to tier-2-helmet\n"
                "** </wiki-tier-3-body-armor:1214195292581265422> :** For detail related to tier-3-body-armor\n"
                "** </wiki-tier-3-helmet:1214195292854026302> :** For detail related to tier-3-helmet\n"
                "** </wiki-tier-4-body-armor:1214195292581265423> :** For detail related to tier-4-body-armor\n"
                "** </wiki-tier-4-helmet:1214195292854026304> :** For detail related to tier-4-helmet\n"
                "** </wiki-tier-5-body-armor:1214195292581265424> :** For detail related to tier-5-body-armor\n"
                "** </wiki-tier-5-helmet:1214195292854026305> :** For detail related to tier-5-helmet\n"
                "** </wiki-tier-6-body-armor:1214195292581265425> :** For detail related to tier-6-body-armor\n"
                "** </wiki-tier-6-helmet:1214195292854026306> :** For detail related to tier-6-helmet\n"
    ,
    color=discord.Color.dark_gray()
)
async def help_embed():
    return embed