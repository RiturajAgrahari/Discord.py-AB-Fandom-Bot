import discord
import fandom

fandom.set_wiki('arena-breakout')

CACHE = {}


async def get_content(PAGE):
    search = fandom.search(PAGE, results=1)

    page_name = search[0][0]
    page_no = search[0][1]
    # print(page_name, page_no)
    page = fandom.page(title=page_name)
    page2 = fandom.page(pageid=page_no)
    content = page.content
    # print(content)
    image = page.images
    return content, image


async def get_average(title):
    if title in CACHE.keys():
        content = CACHE[title]["content"]
        image = CACHE[title]["image"]
    else:
        content, image = await get_content(title)
        CACHE[title] = {"content": content, "image": image}

    infobox = content['infobox'].split("\n")

    embed = discord.Embed(
        title=content['title'],
        description=content['content'],
        color=discord.Color.yellow()
    )
    # print(image)
    embed.set_thumbnail(url=image[0])

    if infobox[2].lower() == 'statistics':
        for i in range(3, len(infobox), 2):
            embed.add_field(name=infobox[i], value=infobox[i + 1], inline=True)
        return embed
    else:
        for i in range(2, len(infobox), 2):
            embed.add_field(name=infobox[i], value=infobox[i + 1], inline=True)
        return embed
